import re


def is_digit(n):
    return bool(re.match('^[0-9](?!\\n)$', n))
