import re


def is_digit(n):
    pattern = re.compile('^\\d(?!\\s)$')
    return bool(re.match(pattern, n))
