import re


def is_digit(n):
    return True if not re.match('^\\d$', n, re.M) is None and len(n) == 1 else False
