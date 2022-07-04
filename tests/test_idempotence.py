from json_flattener import flatten_json, unflatten_json
from random import randint, random, seed

def idempotence(obj):
    assert obj == unflatten_json(flatten_json(obj))

def test_bool():
    idempotence(True)
    idempotence(False)

def test_null():
    idempotence(None)

def test_int():
    seed(31337)
    for _ in range(100):
        idempotence(randint(-100, 100))

def test_float():
    seed(31337)
    for _ in range(100):
        idempotence(random())

def test_string():
    idempotence("")
    idempotence('"')
    idempotence("'")
    idempotence("\n")
    idempotence("\t")
    idempotence("\r")
    idempotence("\a")
    idempotence("\b")
    idempotence('B[+\x7fq')
    idempotence("AADADFAFAF")


def test_list():
    idempotence([])
    idempotence([1])
    idempotence([1, 2])
    idempotence([3, 4, 6])
    idempotence([True, None, 6, 7.0, "ciao"])
    idempotence([True, None, 6, 7.0, "ciao", [1, 2, {"a.:c'\"":[]}]])

def test_dict():
    idempotence({})
    idempotence({"a":1})
    idempotence({"1.0":1})