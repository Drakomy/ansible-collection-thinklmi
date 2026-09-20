#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    AUTH_COMPONENTS,
    AUTH_WRITE_PROPERTIES,
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def main():
    module = AnsibleModule(
        argument_spec={
            "component": {
                "type": "str",
                "required": True,
                "choices": AUTH_COMPONENTS
            },
            "property": {
                "type": "str",
                "required": True,
                "choices": AUTH_WRITE_PROPERTIES
            },
            "value": {
                "type": "str",
                "required": True
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
        category = "authentication"
        component = module.params["component"]
        property_name = module.params.get("property")
        value= module.params.get("value")

        client.write_value(
            category=category,
            component=component,
            property_name=property_name,
            value=value
        )
        module.exit_json(
            changed=True,
            component=component,
            property=property_name
        )
    except SysFSThinkLMIError as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
