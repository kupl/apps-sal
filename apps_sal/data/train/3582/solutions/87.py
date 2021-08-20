import re


def is_digit(n):
    return bool(re.findall('^\\d{1}\\Z', n))
