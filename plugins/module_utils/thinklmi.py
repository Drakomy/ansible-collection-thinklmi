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

AUTH_PROPERTIES = [
    "index",
    "is_enabled",
    "level",
    "max_password_length",
    "mechanism",
    "min_password_length",
    "role",
]

POWER_PROPERTIES = [
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

ATTRIBUTE_COMPONENTS = [
    'After Power Loss',
    'Intel(R) Virtualization Technology',
    'Serial Port1 Address',
    'AlarmDate(MM\\DD\\YYYY)',
    'Intel Thunderbolt Technology',
    'Smart Power On',
    'Alarm Day of Week',
    'Internal Speaker',
    'Smart USB Protection',
    'AlarmTime(HH:MM:SS)',
    'Monday',
    'SOL Configuration',
    'Allow Flashing BIOS to a Previous Version',
    'Network Offline Locker',
    'Startup Sequence',
    'ASPM Support',
    'Onboard Audio Controller',
    'Sunday',
    'Automatic Boot Sequence',
    'Onboard Ethernet Controller',
    'TCG Security Device',
    'Boot Mode',
    'OS Optimized Defaults',
    'TFTP Window Size',
    'Boot Up Num-Lock Status',
    'Password Count Exceeded Error',
    'Thursday',
    'C1E Support',
    'PCIe 8x Slot Speed',
    'Tuesday',
    'Chassis Intrusion Detection',
    'pending_reboot',
    'Turbo Mode',
    'Computrace Module Activation',
    'POP Changeable by User',
    'TxT',
    'Configuration Change Detection',
    'Press <Ctrl-P> to Enter MEBx',
    'USB Enumeration Delay',
    'Configure SATA as',
    'Primary Boot Sequence',
    'USB Legacy Support',
    'Core Multi-Processing',
    'PXE IPV4 Network Stack',
    'USB Port 1',
    'CSM',
    'PXE IPV6 Network Stack',
    'USB Port 2',
    'C State Support',
    'PXE Option ROM',
    'USB Port 3',
    'Device Guard',
    'Rear USB Ports',
    'USB Port 4',
    'Dust Shield Alert',
    'Require Admin. Pass. For F12 Boot',
    'USB Port 5',
    'EIST Support',
    'Require Admin. Pass. when Flashing',
    'USB Port 6',
    'Enhanced Power Saving Mode',
    'Require HDP on System Boot',
    'USB Provisioning',
    'Error Boot Sequence',
    'Require POP on Restart',
    'USB Support',
    'Friday',
    'Require POP on System Boot',
    'UserDefinedAlarmTime',
    'Front USB Ports',
    'SATA Controller',
    'VT-d',
    'Hard Disk Pre-delay',
    'SATA Drive 1',
    'Wake from Serial Port Ring',
    'ICE Performance Modes',
    'Saturday',
    'Wake on LAN',
    'ICE Thermal Alert',
    'save_settings',
    'Wake Up on Alarm',
    'Intel(R) Manageability Control',
    'Secure Boot',
    'Wednesday',
    'Intel(R) SGX Control',
    'Security Chip 2.0',
    'Windows UEFI Firmware Update',
    'Intel(R) SIPP Support',
    'Select Active Video'
]

ATTIBUTE_PROPERTIES = [
    'current_value',
    'display_name',
    'possible_values',
    'type'
]

class SysFSThinkLMIError(RuntimeError):
    """Raised when a Lenovo firmware attribute cannot be read or written."""

class SysFSThinkLMI:
    BASE_PATH = "/sys/devices/virtual/firmware-attributes/thinklmi"

    def __init__(self, base_path: str = BASE_PATH) -> None:
        self.base_path = Path(base_path)
        if not self.base_path.exists():
            raise SysFSThinkLMIError(f"sysfs base path does not exist: {self.base_path}")

    def _property_path(self, category: str, component: str, property_name: str) -> Path:
        path = self.base_path / category
        if component:
            path /= component
    
        path /= property_name
        if not path.exists():
            raise SysFSThinkLMIError(f"Property does not exist: {path}")
        return path

    def read_value(
        self,
        category: str,
        component: str,
        property_name: Optional[str] = None,
    ) -> str:
        path = self._property_path(category, component, property_name)
        try:
            data = path.read_text(encoding="utf-8").strip()
        except OSError as e:
            raise SysFSThinkLMIError(f"Error reading property: {str(e)}")
        return data
