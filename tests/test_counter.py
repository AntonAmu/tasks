from counter import *
from unittest import mock
from io import StringIO
import sys


def test_parse_arg():
    args = parse_arg(['1Hello World!@#'])
    assert args.__dict__ == {f'{ARGUMENT_NAME}': '1Hello World!@#'}


def test_count_letters_string_with_letters():
    assert count_letters('1Hello World!@#') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


def test_count_letters_string_without_letters():
    assert count_letters(' !') == {}


def test_counter_main_string_with_letters():
    with mock.patch.object(sys, 'argv', ['file', 'Hello World!']):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == str({'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}) + '\n'


def test_counter_main_string_without_letters():
    with mock.patch.object(sys, 'argv', ['file', ' !']):
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            assert mock_stdout.getvalue() == 'String has to have at least one letter\n'
