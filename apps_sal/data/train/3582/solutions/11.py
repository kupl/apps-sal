import re


def is_digit(string):
    return bool(re.fullmatch(r"\d", string))
