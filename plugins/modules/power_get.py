#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import annotations

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.drakomy.thinklmi.plugins.module_utils.thinklmi import (
    SysFSThinkLMI,
    SysFSThinkLMIError,
)

def main():
    module = AnsibleModule(
        argument_spec={
            "property": {
                "type": "str",
                "required": True,
                "choices": [
                    "async",
                    "autosuspend_delay_ms",
                    "control",
                    "runtime_active_kids",
                    "runtime_active_time",
                    "runtime_enabled",
                    "runtime_status",
                    "runtime_suspended_time",
                    "runtime_usage"
                ],
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
        property_name = module.params.get("property")
        result = client.read_value(category="power", component=None, property_name=property_name)
        module.exit_json(changed=False, property=property_name, result=result)
    except SysFSThinkLMIError as exc:
        module.fail_json(msg=str(exc))


if __name__ == "__main__":
    main()
