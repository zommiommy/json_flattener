import sys
import atheris
import math

with atheris.instrument_imports():
  import json
  import json_flattener

def consume_json(fdp):
    type_num = fdp.ConsumeIntInRange(0, 4)
    if type_num == 0:
        return None
    elif type_num == 1:
        return fdp.ConsumeBool()
    elif type_num == 2:
        return fdp.ConsumeInt(fdp.ConsumeIntInRange(0, 8))
    elif type_num == 3:
        return fdp.ConsumeFloat()
    elif type_num == 4:
        return fdp.ConsumeString(fdp.ConsumeIntInRange(0, 1024))
    elif type_num == 5:
        return {
            fdp.ConsumeString(fd.ConsumeIntInRange(0, 1024)):consume_json(fdp)
            for _ in fdp.ConsumeIntInRange(0, 1024)
        }
    elif type_num == 6:
        return [
            consume_json(fdp)
            for _ in fdp.ConsumeIntInRange(0, 1024)
        ]
    else:
        raise ValueError("Wrong generation of json with type_num {}".format(type_num))


def harness(data):
    fdp = atheris.FuzzedDataProvider(data)
    obj = consume_json(fdp)
    flattened = json_flattener.flatten_json(obj)
    unflattened = json_flattener.unflatten_json(flattened)
    
    # nan arn't equal to themselves :)
    if isinstance(obj, float) and math.isnan(obj) == math.isnan(unflattened):
        return
    
    assert obj == unflattened

atheris.Setup(sys.argv, harness)
atheris.Fuzz()