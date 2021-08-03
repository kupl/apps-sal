import re


def is_digit(n):
    return bool(re.match(r'\A\d\Z', str(n)))
