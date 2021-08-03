import re


def is_digit(n):
    print(n)
    if n.isdigit():
        return True if re.match('^[0-9]$', n) else False
    else:
        return False
