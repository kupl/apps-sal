import re


def is_digit(n):
    if len(n) > 1:
        return False
    elif re.match('[0-9]', n):
        return True
    else:
        return False
