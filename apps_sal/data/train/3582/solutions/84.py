import re


def is_digit(n):
    return bool(re.match('\\A\\d\\Z', str(n)))
