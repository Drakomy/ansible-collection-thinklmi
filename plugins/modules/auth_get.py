#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    AUTH_COMPONENTS,
    AUTH_PROPERTIES,
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def main():
    module = AnsibleModule(
        argument_spec={
            "component": {
                "type": "str",
                "required": True,
                "choices": AUTH_COMPONENTS,
            },
            "property": {
                "type": "str",
                "required": True,
                "choices": AUTH_PROPERTIES,
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
        component = module.params["component"]
        property_name = module.params.get("property")
        result = client.read_value(category="authentication", component=component, property_name=property_name)
        module.exit_json(changed=False, component=component, property=property_name, result=result)
    except SysFSThinkLMIError as exc:
        module.fail_json(msg=str(exc))


if __name__ == "__main__":
    main()
