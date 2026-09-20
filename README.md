# Ansible Collection - drakomy.thinklmi

This collection uses the Lenovo ThinkLMI sysfs entries already present in the Linux kernel to automate BIOS configuration from Ansible.

## Purpose

The collection works with the existing ThinkLMI sysfs hierarchy in Linux. It does not define a new BIOS model; it exposes the kernel-managed data so it can be read and changed through Ansible.

## Todo
- check mode
- replace static list
- unit test
- refactor module pattern

## Data model

The Linux kernel exposes ThinkLMI values under a small hierarchy:

- `category`: top-level data group such as `attributes`, `authentication`, or `power`
- `component`: the named item inside that category
- `property`: the value or field associated with that component

The code reads and writes from `/sys/devices/virtual/firmware-attributes/thinklmi` using this pattern.

## Collection scope

The collection includes modules for:

- reading BIOS attribute values
- writing BIOS attribute values
- reading authentication values
- writing authentication values
- reading power values

For module-specific details, see the module reference in `plugins/modules/README.md`.

## Common BIOS attributes

The root README keeps the attribute list as a reference for the ThinkLMI `attributes` tree. These names are commonly seen on Lenovo M920Q and M720Q systems.

- After Power Loss
- Alarm Day of Week
- AlarmDate(MM\DD\YYYY)
- AlarmTime(HH:MM:SS)
- Allow Flashing BIOS to a Previous Version
- ASPM Support
- Automatic Boot Sequence
- Boot Mode
- Boot Up Num-Lock Status
- C State Support
- C1E Support
- Chassis Intrusion Detection
- Computrace Module Activation
- Configuration Change Detection
- Configure SATA as
- Core Multi-Processing
- CSM
- Device Guard
- Dust Shield Alert
- EIST Support
- Enhanced Power Saving Mode
- Error Boot Sequence
- Friday
- Front USB Ports
- Hard Disk Pre-delay
- ICE Performance Modes
- ICE Thermal Alert
- Intel Thunderbolt Technology
- Intel(R) Manageability Control
- Intel(R) SGX Control
- Intel(R) SIPP Support
- Intel(R) Virtualization Technology
- Internal Speaker
- Monday
- Network Offline Locker
- Onboard Audio Controller
- Onboard Ethernet Controller
- OS Optimized Defaults
- Password Count Exceeded Error
- PCIe 8x Slot Speed
- pending_reboot
- POP Changeable by User
- Press <Ctrl-P> to Enter MEBx
- Primary Boot Sequence
- PXE IPV4 Network Stack
- PXE IPV6 Network Stack
- PXE Option ROM
- Rear USB Ports
- Require Admin. Pass. For F12 Boot
- Require Admin. Pass. when Flashing
- Require HDP on System Boot
- Require POP on Restart
- Require POP on System Boot
- SATA Controller
- SATA Drive 1
- Saturday
- save_settings
- Secure Boot
- Security Chip 2.0
- Select Active Video
- Serial Port1 Address
- Smart Power On
- Smart USB Protection
- SOL Configuration
- Startup Sequence
- Sunday
- TCG Security Device
- TFTP Window Size
- Thursday
- Tuesday
- Turbo Mode
- TxT
- USB Enumeration Delay
- USB Legacy Support
- USB Port X
- USB Provisioning
- USB Support
- UserDefinedAlarmTime
- VT-d
- Wake from Serial Port Ring
- Wake on LAN
- Wake Up on Alarm
- Wednesday
- Windows UEFI Firmware Update

## AI disclosure

The documentation was drafted with AI assistance. The code was written manually and may not be optimal.
