from dataclasses import dataclass, field, make_dataclass, is_dataclass
from typing import Any, List, get_type_hints

def auto_dataclass(name: str, data: dict):
    fields = []

    for key, value in data.items():
        if isinstance(value, dict):
            nested_class = auto_dataclass(f"{name}_{key.capitalize()}", value)
            fields.append((key, nested_class))
        elif isinstance(value, list):
            if value and isinstance(value[0], dict):
                nested_class = auto_dataclass(f"{name}_{key.capitalize()}", value[0])
                fields.append((key, List[nested_class], field(default_factory=list)))
            else:
                fields.append((key, List[type(value[0]) if value else Any], field(default_factory=list)))
        else:
            fields.append((key, type(value)))

    return make_dataclass(name, fields)

def dataclass_from_dict(cls, data):
    kwargs = {}
    hints = get_type_hints(cls)

    for key, value in data.items():
        if key not in hints:
            continue

        expected_type = hints[key]

        if is_dataclass(expected_type):
            kwargs[key] = dataclass_from_dict(expected_type, value)
        elif getattr(expected_type, '__origin__', None) == list:
            subtype = expected_type.__args__[0]
            if is_dataclass(subtype):
                kwargs[key] = [dataclass_from_dict(subtype, item) for item in value]
            else:
                kwargs[key] = value
        else:
            kwargs[key] = value

    return cls(**kwargs)

