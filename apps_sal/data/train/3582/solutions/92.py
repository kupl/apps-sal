import re


def is_digit(n):
    if len(n) != 1:
        return False
    else:
        match = re.findall('[0-9]', n)
        if len(match) == 1:
            return True
        else:
            return False
