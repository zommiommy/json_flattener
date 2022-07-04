from json_flattener import split_with_escaping

def test_splitter():
    assert list(split_with_escaping("a.b:c")) == ["a", "b", "c"]
    assert list(split_with_escaping('a."b.c".d:aaaaa')) == ["a", "b.c", "d", "aaaaa"]
    assert list(split_with_escaping('a."b:c".d:aaaaa')) == ["a", "b:c", "d", "aaaaa"]
    assert list(split_with_escaping(r'a."b\"c".d:aaaaa')) == ["a", "b\"c", "d", "aaaaa"]
    assert list(split_with_escaping('a."b\'c".d:aaaaa')) == ["a", "b'c", "d", "aaaaa"]
    assert list(split_with_escaping('a."b.c":aaaaa')) == ["a", "b.c", "aaaaa"]
