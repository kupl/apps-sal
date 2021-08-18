import re


def is_digit(n):
    return re.fullmatch(r"\d", n) != None
