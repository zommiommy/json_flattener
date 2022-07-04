# json_flattener
A python package to flatten a JSON into a list of strings and back

```python
> from flatten_json import flatten_json

# Base types
> flatten_json(True)
["true"]

> flatten_json(False)
["false"]

> flatten_json(None)
["null"]

> flatten_json(1.0)
["1.0"]

> flatten_json("ciao")
["\"ciao\""]

> flatten_json({})
["{}"]

> flatten_json({"a":1})
["a:1"]

> flatten_json([])
["[]"]

> flatten_json([1, 2, 3])
["[]", "0:1", "1:2", "2:3"]

# Nesting
> flatten_json({"a":{"b":1}})
["a.b:1"]

> flatten_json({"a":[1, 2, 3]})
["a:[]", "a.0:1", "a.1:2", "a.2:3"]

> flatten_json([1, 2, [3, 4]])
["[]", "0:1", "1:2", "2:[]", "2.0:3", "2.1:4"]

> flatten_json([1, 2, [3, 4], [5, 6]])
["[]", "0:1", "1:2", "2:[]", "2.0:3", "2.1:4", "3:[]", "3.0:5", "3.1:6",]

> flatten_json([True, None, 6, 7.0, "ciao", [1, 2, {"a.:c'\"":[]}]])
['[]', '0:true', '1:null', '2:6', '3:7.0', '4:"ciao"', '5:[]', '5.0:1', '5.1:2', '5.2."a.:c\'\\"":[]']

# list indices are actually priorities
> assert unflatten_json(["[]", "0:1", "1:1"]) == unflatten_json(["[]", "0:1", "2:1"])

# the keys of dicts can be escaped with quotes, this also is needed to
# escape the special chars . and :
> assert unflatten_json(['a:1']) == unflatten_json(['"a":1'])
> assert unflatten_json(['a.b:1']) == unflatten_json(['"a"."b":1'])
> assert unflatten_json(["a.\"b.c\".d:1"]) == {"a":{"b.c":{"d":1}}}
> assert unflatten_json(['"a\'.:d":1']) == {"a'.:d":1}
> assert unflatten_json(['"a\'\\\".:d":1']) == {"a'\".:d":1}
```

# Fuzzing
Install atheris
```shell
pip3 install atheris
```
Run a fuzzer:
```shell
python fuzz_structured_idempotence.py
```
This tests that the following assertion holds for all possible jsons:
```python
from flatten_json import flatten_json, unflatten_json
assert obj == unflatten_json(flatten_json(obj))
```