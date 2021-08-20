import re


def is_digit(n):
    if re.match('\\d', n) and len(n) == 1:
        return True
    return False
