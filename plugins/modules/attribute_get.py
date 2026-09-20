#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    ATTRIBUTE_READ_PROPERTIES,
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def main():
    module = AnsibleModule(
        argument_spec={
            "component": {
                "type": "str",
                "required": True
            },
            "property": {
                "type": "str",
                "required": True,
                "choices": ATTRIBUTE_READ_PROPERTIES
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
        property_name = module.params.get("property")

        client.validate_component(
            category=category,
            component=component
        )

        result = client.read_value(
            category=category,
            component=component,
            property_name=property_name
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
