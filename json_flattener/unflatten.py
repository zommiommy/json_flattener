import json
from typing import List

from .split import split_with_escaping

class DictList(dict):
    """Wrapper for a dict that carries the information that this will 
    have to be converted to a list.
    by convention all indexable values are dictionaries.
    we distingish between dictionaries and list by the types of
    the keys. specifically in JSON keys HAVE TO BE strings
    so to check if a dict is actually a list we check if the keys
    are integers.
    """
    pass

def listify(obj):
    """Recursively walk the json and convert any DictList to an actual list"""
    
    if isinstance(obj, list):
        return [listify(x) for x in obj]

    if isinstance(obj, DictList):
        return [
            listify(x[1]) 
            for x in sorted(
                (int(key), value)
                for key, value in obj.items()
            )
        ]

    if not isinstance(obj, dict):
        return obj

    return {
        key:listify(value)
        for key, value in obj.items()
    }    

def unflatten_json(args: List[str]):
    result = {}
    for arg in args:
        # if it's just a valid json, parse it
        try:
            result = json.loads(arg)
            if isinstance(result, list):
                result = DictList(enumerate(result))
            continue
        except json.JSONDecodeError as e:
            pass

        *path, last, value = list(split_with_escaping(arg))
        obj = result
        for key in path:
            obj = obj.setdefault(key, {})

        try:
            val = json.loads(value)
            if isinstance(val, list):
                val = DictList(enumerate(val))
        except json.JSONDecodeError as e:
            raise ValueError(
                "Cannot parse {} as a json value. {}".format(
                    repr(value), e
                ))

        obj[last] = val


    return listify(result)