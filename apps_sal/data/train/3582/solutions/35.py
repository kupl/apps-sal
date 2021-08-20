import re


def is_digit(n):
    print(n)
    return True if re.fullmatch('\\d', n) else False
