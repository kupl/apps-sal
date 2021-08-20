import re


def is_digit(n):
    print(n)
    if '\n' in n:
        return False
    return bool(re.match('^[0-9]$', n))
