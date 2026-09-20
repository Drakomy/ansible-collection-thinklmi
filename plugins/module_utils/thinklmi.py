# -*- coding: utf-8 -*-

from __future__ import annotations

from pathlib import Path
from typing import Optional

AUTH_COMPONENTS = [
    "Admin",
    "HDD",
    "NVMe",
    "Power-on",
    "System"
]

AUTH_READ_PROPERTIES = [
    "index",
    "is_enabled",
    "level",
    "max_password_length",
    "mechanism",
    "min_password_length",
    "role",
]

AUTH_WRITE_PROPERTIES = [
    "current_password",
    "new_password"
]

POWER_READ_PROPERTIES = [
    "async",
    "autosuspend_delay_ms",
    "control",
    "runtime_active_kids",
    "runtime_active_time",
    "runtime_enabled",
    "runtime_status",
    "runtime_suspended_time",
    "runtime_usage"
]

ATTRIBUTE_READ_PROPERTIES = [
    'current_value',
    'display_name',
    'possible_values',
    'type'
]

class SysFSThinkLMIError(RuntimeError):
    """Raised when a Lenovo firmware attribute cannot be read or written."""

class SysFSThinkLMI:
    BASE_PATH = Path("/sys/devices/virtual/firmware-attributes/thinklmi")

    def __init__(self, base_path: str = BASE_PATH) -> None:
        self.base_path = Path(base_path)
        if not self.base_path.is_dir():
            raise SysFSThinkLMIError(
                f"sysfs base path does not exist: {self.base_path}"
            )

    def _property_path(self, category: str, component: str, property_name: str) -> Path:
        path = self.base_path / category
        if component:
            path /= component

        path /= property_name
        if not path.exists():
            raise SysFSThinkLMIError(
                f"Property does not exist: {path}"
            )
        return path

    def read_value(
        self,
        category: str,
        component: str,
        property_name: str,
    ) -> str:
        path = self._property_path(category, component, property_name)
        try:
            return path.read_text(encoding="utf-8").strip()
        except OSError as e:
            raise SysFSThinkLMIError(
                f"Error reading property {path}: {e}"
            ) from e

    def read_attribute_property_possible_values(
        self,
        category: str,
        component: str,
    ) -> list[str]:
        value = self.read_value(
            category=category,
            component=component,
            property_name="possible_values",
        )

        return value.split(";")

    def write_value(
        self,
        category: str,
        component: str,
        property_name: str,
        value: str,
    ) -> None:
        path = self._property_path(category, component, property_name)
        try:
            path.write_text(value, encoding="utf-8")
        except OSError as e:
            raise SysFSThinkLMIError(
                f"Error writing property {path}: {e}"
            ) from e

    @staticmethod
    def list_components(category: str, base_path: str = BASE_PATH) -> list[str]:
        root = Path(base_path) / category
        if not root.exists():
            return []
        return sorted(item.name for item in root.iterdir() if item.is_dir())
