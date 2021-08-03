import re


def is_digit(n):
    match = re.compile('[0-9]').fullmatch(n)
    if not match:
        return False
    return match.group() == n
