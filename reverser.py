import sys
import argparse
from constants.constants_for_reverser import MESSAGE, OPTIONAL_ARGUMENT_NAME, REQUIRED_ARGUMENT_NAME


class Reverser:
    """
    Class that revers the given string
    """

    def __init__(self, _all: bool):
        self._all = _all

    @staticmethod
    def extract_letters(input_string: str) -> str:
        """
        Method that extract all letters from the given string
        :param input_string: str
        :return: str
        """
        letters = ''
        for char in input_string:
            if not char.isalpha():
                continue
            letters += char
        return letters

    @staticmethod
    def reverse_string(string: str) -> str:
        """
        Method that reverse order of given string letters and separates each char with new line.
        :param string: str
        :return: str
        """
        if len(string) == 1:
            return string
        else:
            return Reverser.reverse_string(string[1:]) + '\n' + string[0]

    def reverse(self, input_string: str) -> str:
        """
        Method that reverse given string according to value of flag (True or False).
        If flag == True then this method reverses all char in the sting, otherwise
        it extracts only letters and reverses them.
        :param input_string: str
        :return: str
        """
        if self._all:
            output = self.reverse_string(input_string)
            return output
        else:
            letters = self.extract_letters(input_string)
            if letters:
                output = self.reverse_string(letters)
                return output
            else:
                return MESSAGE


def parse_arg(args: list) -> object:
    """
    Function that parse arguments from command line
    and return the object with attribute equal this argument.
    :param args: list
    :return: object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(REQUIRED_ARGUMENT_NAME)
    parser.add_argument('--' + OPTIONAL_ARGUMENT_NAME, action='store_true', default=False)
    return parser.parse_args(args)


def main():
    args = parse_arg(sys.argv[1:]).__dict__
    print(Reverser(args.get(OPTIONAL_ARGUMENT_NAME)).reverse(args.get(REQUIRED_ARGUMENT_NAME)))


if __name__ == '__main__':
    main()
