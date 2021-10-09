import sys
import argparse
from constants.constants_for_counter import MESSAGE, ARGUMENT_NAME


def main():
    args = parse_arg(sys.argv[1:])
    output = count_letters(**args.__dict__)
    if output:
        print(output)
    else:
        print(MESSAGE)


def parse_arg(args: list) -> object:
    """
    Function that parse argument from command line
    and return the object with attribute equal this argument.
    :param args: list
    :return: object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(ARGUMENT_NAME)
    return parser.parse_args(args)


def count_letters(input_string: str) -> dict:
    """
    Function that count the number of each unique letter in the given string.
    :param input_string: str
    :return: dict
    """
    result = {}
    input_string = input_string.lower()
    for char in input_string:
        if not char.isalpha():
            continue
        result[char] = result.get(char, 0) + 1
    return result


if __name__ == '__main__':
    main()
