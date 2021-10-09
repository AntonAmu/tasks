from reverser import *
import pytest


def test_extract_letters():
    assert Reverser.extract_letters("Hello World!") == 'HelloWorld'


def test_reverse_string():
    assert Reverser.reverse_string("Tom and Jerry") == 'y\nr\nr\ne\nJ\n \nd\nn\na\n \nm\no\nT'


@pytest.mark.parametrize('input_, out, flag', [("Hello World!", '!\nd\nl\nr\no\nW\n \no\nl\nl\ne\nH', True),
                                               ("Hello World!", 'd\nl\nr\no\nW\no\nl\nl\ne\nH', False),
                                               (" !", 'String has to have at least one letter', False)])
def test_reverse_string_with_letters_flag_true(input_, out, flag):
    assert Reverser(flag).reverse(input_) == out

