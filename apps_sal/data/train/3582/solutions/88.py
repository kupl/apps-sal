import re


def is_digit(n):
    if re.search('[0-9]{1}', n) is None:
        return False
    elif len(n) >= 2:
        return False
    else:
        return True
