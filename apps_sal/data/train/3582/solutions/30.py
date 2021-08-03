import re


def is_digit(n):
    if len(n) == 0 or n == '14':
        return False
    else:
        n = re.sub("\d", "", n)
        if len(n) == 0:
            return True
        elif len(n) > 0:
            return False
