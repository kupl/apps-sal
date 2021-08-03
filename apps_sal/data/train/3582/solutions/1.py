import re


def is_digit(n):
    return bool(re.match("\d\Z", n))
