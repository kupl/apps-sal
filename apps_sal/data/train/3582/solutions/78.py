import re


def is_digit(n):
    return re.fullmatch('\\d', n) != None
