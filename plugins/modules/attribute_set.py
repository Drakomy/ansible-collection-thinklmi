#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def _validate_value(
    client: SysFSThinkLMI,
    category: str,
    component: str,
    value: str
) -> None:
    possible_values = client.read_attribute_property_possible_values(
        category=category,
        component=component,
    )

    if value not in possible_values:
        raise SysFSThinkLMIError(
                f"Invalid value '{value}' for component '{component}'."
                f"Possible values: {possible_values}"
        )

def main():
    module = AnsibleModule(
        argument_spec={
            "component": {
                "type": "str",
                "required": True
            },
            "value": {
                "type": "str",
                "required": True,
            },
            "base_path": {
                "type": "str",
                "required": False,
                "default": SysFSThinkLMI.BASE_PATH
            },
        },
        supports_check_mode=False,
    )

    try:
        client = SysFSThinkLMI(base_path=module.params["base_path"])
        category = "attributes"
        component = module.params["component"]
        property_name = "current_value"
        value = module.params.get("value")

        client.validate_component(
            category=category,
            component=component)

        _validate_value(
            client=client,
            category=category,
            component=component,
            value=value
        )

        curr_value = client.read_value(
            category=category,
            component=component,
            property_name=property_name
        )

        if curr_value == value:
            module.exit_json(
                changed=False,
                component=component,
                property=property_name,
                value=value
            )
        else:
            client.write_value(
                category=category,
                component=component,
                property_name=property_name,
                value=value
            )
            module.exit_json(
                changed=True,
                component=component,
                property=property_name,
                value=value
            )
    except SysFSThinkLMIError as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
