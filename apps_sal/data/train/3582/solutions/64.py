import re


def is_digit(n):
    print(n)
    return True if re.match('\\d', n) and len(n) == 1 else False
