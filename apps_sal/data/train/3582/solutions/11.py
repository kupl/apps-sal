import re


def is_digit(string):
    return bool(re.fullmatch('\\d', string))
