import re


def is_digit(n):
    x = re.match('^\\d', n)
    if len(n) == 1 and x:
        return True
    else:
        return False
