import re


def is_digit(n):
    if n:
        return list(n) == re.findall('\\d+', n)
    return False
