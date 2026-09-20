#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    POWER_READ_PROPERTIES,
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def main():
    module = AnsibleModule(
        argument_spec={
            "property": {
                "type": "str",
                "required": True,
                "choices": POWER_READ_PROPERTIES
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
        category = "power"
        property_name = module.params.get("property")

        result = client.read_value(
            category=category,
            component=None,
            property_name=property_name
        )
        module.exit_json(changed=False, property=property_name, result=result)
    except SysFSThinkLMIError as e:
        module.fail_json(msg=str(e))


if __name__ == "__main__":
    main()
