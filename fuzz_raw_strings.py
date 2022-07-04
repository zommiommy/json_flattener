import sys
import atheris
import math

with atheris.instrument_imports():
  import json
  import json_flattener

def harness(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    args = [
        fdp.ConsumeString(fdp.ConsumeIntInRange(0, 1024))
        for _ in range(fdp.ConsumeInt(fdp.ConsumeIntInRange(0, 8)))
    ]
    print(args)
    json_flattener.unflatten_json(args)

atheris.Setup(sys.argv, harness)
atheris.Fuzz()