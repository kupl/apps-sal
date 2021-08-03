import re


def is_digit(n):
    print(n)
    if re.fullmatch('^[0-9]$', n) == None:
        return False
    return True
