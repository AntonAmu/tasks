import dotenv
import os
import sys
import argparse


class Cryptographer:
    """
    Class that encodes and decodes messages using offsetting the letters.
    """
    def __init__(self):
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.__key = os.environ.get('key')
        self.__salt = os.environ.get('salt')

    def encode(self, text: str) -> str:
        """
        Method that takes message, encodes it and return encoded one.
        :param text: str
        :return: str
        """
        enc_msg = ''
        text += self.__salt
        for char in text:
            num = ord(char) + int(self.__key)
            encoded_char = chr(num if num < 1114111 else num - 1114111)
            enc_msg += encoded_char
        return enc_msg

    def decode(self, enc_msg: str) -> str:
        """
        Method that takes encoded message, decode in and return decoded one.
        :param enc_msg:
        :return:
        """
        text = ''
        for char in enc_msg:
            num = ord(char) - int(self.__key)
            decoded_char = chr(num if num > 0 else 1114111 + num)
            text += decoded_char
        text = text[::-1].replace(self.__salt[::-1], '', 1)
        return text[::-1]


def parse_arg(args: list) -> object:
    """
    Function that parse arguments from command line
    and return the object with attribute equal this argument.
    :param args: list
    :return: object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    parser.add_argument('action', choices=['decode', 'encode'])
    return parser.parse_args(args)


def main():
    args = parse_arg(sys.argv[1:]).__dict__
    msg = Cryptographer().__getattribute__(args.get('action'))(args.get('text'))
    print(msg)


if __name__ == '__main__':
    main()
