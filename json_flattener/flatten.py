import json
from typing import List, Tuple

def flatten_json(obj) -> List[str]:
    return [
        key + ":" + value
        if key is not None else value
        for key, value in _converter(obj)
    ]

def _converter(obj) -> List[Tuple[str, str]]:
    if obj is None:
        return [(None, "null")]
    elif isinstance(obj, (bool, int, float)):
        # ensure_ascii is needed to aboid issue #94527
        # https://github.com/python/cpython/issues/94527
        return [(None, json.dumps(obj, ensure_ascii=False))]
    elif isinstance(obj, str):
        return [(None, json.dumps(obj, ensure_ascii=False))]
    elif isinstance(obj, dict):
        res = []
        for key, value in obj.items():
            key = json.dumps(key)
            for sub_key, val in _converter(value):
                if sub_key is None:
                    res.append((key, val))
                else:
                    res.append((key + "." + sub_key, val))
        return res
    elif isinstance(obj, list):
        res = [(None, "[]")]
        for i, value in enumerate(obj):
            for sub_key, val in _converter(value):
                if sub_key is None:
                    res.append((str(i), val))
                else:
                    res.append((str(i) + "." + sub_key, val))
        return res
    else:
        raise ValueError(
            "The given value {} of type {} is not JSON serializable".format(
            obj, obj.__class__,
        ))