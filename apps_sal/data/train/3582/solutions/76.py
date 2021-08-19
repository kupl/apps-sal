import re


def is_digit(n):
    match = re.findall('[\\d]', n)
    return match[0] == n if match else False
