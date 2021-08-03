import re


def is_digit(n):
    if n.isdigit() == False or len(n) >= 2:
        return False
    return bool(re.search(r'[0-9]', n))
