import re


def is_digit(n):
    regex = '^\d$'

    if (re.search(regex, n)) and n.isdigit():
        return True
    else:
        return False
