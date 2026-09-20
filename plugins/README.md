# ThinkLMI Plugin

This page documents each module in terms of the ThinkLMI data model used by the project:

- `category`
- `component`
- `property`

The modules read or write values from the Linux ThinkLMI sysfs tree under `/sys/devices/virtual/firmware-attributes/thinklmi` or `/sys/class/firmware-attributes/thinklmi`.

## attribute_get

Reads a property for a component in the `attributes` category.

The module expects:

- `component`: the BIOS attribute name
- `property`: the field to read, such as `current_value`, `display_name`, `possible_values`, or `type`

It validates that the component exists before reading the requested property.

## attribute_set

Writes a value to a component in the `attributes` category.

The module expects:

- `component`: the BIOS attribute name
- `value`: the new value to assign

It validates the component and verifies that the value is allowed before writing it to the `current_value` property.

## auth_get

Reads a property for a component in the `authentication` category.

The module expects:

- `component`: the authentication component, such as `Admin`, `HDD`, `NVMe`, `Power-on`, or `System`
- `property`: the field to read, such as `index`, `is_enabled`, `level`, `max_password_length`, `mechanism`, `min_password_length`, `role`

## auth_set

Writes an authentication property for a component in the `authentication` category.

The module expects:

- `component`: the authentication component
- `property`: the field to write, such as `current_password` or `new_password`
- `value`: the value to store

## power_get

Reads a property from the `power` category.

The module expects:

- `property`: the power value to read, such as `async`, `autosuspend_delay_ms`, `control`, `runtime_enabled`, `runtime_status`, or `runtime_usage`

This module does not require a component because the power entries are global values.
