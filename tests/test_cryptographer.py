from cryptographer import Cryptographer


def test_decode_encode():
    assert Cryptographer().decode(Cryptographer().encode('Hello World!')) == 'Hello World!'


def test_encode_limit():
    assert Cryptographer().encode('Hello World!' + chr(1114111)) == 'Khoor#Zruog$\x03Dvgb45noC6K'


def test_decode_limit():
    assert Cryptographer().decode('Khoor#Zruog$\x03Dvgb45noC6K') == 'Hello World!' + chr(1114111)
