#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def _validate_component(
    client: SysFSThinkLMI,
    category: str,
    component: str,
) -> None:
    component_list = SysFSThinkLMI.list_components(
        category=category,
        base_path=client.base_path,
    )

    if component not in component_list:
        raise SysFSThinkLMIError(
            f"Component {component} does not exist. "
            f"List of valid components: {component_list}"
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
        supports_check_mode=True,
    )

    try:
        client = SysFSThinkLMI(base_path=module.params["base_path"])
        category = "attributes"
        component = module.params["component"]
        property_name = "current_value"
        value = module.params.get("value")

        _validate_component(
            client= client,
            category=category,
            component=component)

        _validate_value(
            client=client,
            category=category,
            component=component,
            value=value
        )

        result = client.write_value(
            category=category,
            component=component,
            property_name=property_name,
            value=value
        )
        module.exit_json(
            changed=False,
            component=component,
            property=property_name,
            result=result
        )
    except SysFSThinkLMIError as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
