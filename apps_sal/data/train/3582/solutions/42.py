import re


def is_digit(n):
    if len(n) > 1:
        return False
    if n.isdigit():
        x = re.search('^[0-9]+$', n)
        if x:
            return True
        else:
            return False
    else:
        return False
