from caesar_cipher.caesar import caesar

def test_empty_string():
    assert caesar("", 5, "encode") == ""

def test_negative_shift():
    assert caesar("abc", -1, "encode") == "zab"

def test_decode_large_shift():
    assert caesar("bcd", 27, "decode") == "abc"

def test_case_insensitive():
    assert caesar("AbC".lower(), 1, "encode") == "bcd"
