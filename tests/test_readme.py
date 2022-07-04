import re
from json_flattener import flatten_json, unflatten_json
from random import randint, random, seed


def test_readme():
    # This is bad but it works lol 🤮
    # If one can modify the README can also modify the test code
    # so there shouldn't be any reasonable threat model where this is a 
    # problem

    with open("README.md", "r") as f:
        text = f.read()

    for match in re.finditer(r"> flatten_json\((.+?)\)", text):
        input_obj = eval(match.group(1))
        expected_output = eval(text[match.span()[1] + 1:].split("\n", maxsplit=1)[0])

        flattened = flatten_json(input_obj)
        unflattened = unflatten_json(flattened)
        assert unflattened == input_obj, "Flattened: {} Result:{} Truth:{}".format(
            expected_output, unflattened, input_obj
        )

    for match in re.finditer(r"> assert (.+)", text):
        assert eval(match.group(1))