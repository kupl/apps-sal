import re


def is_digit(n):
    string = re.fullmatch('[1234567890]', n)
    return False if string == None else True
