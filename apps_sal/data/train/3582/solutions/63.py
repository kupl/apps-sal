from re import search


def is_digit(n):
    return bool(search('(^[0-9]$)(?!\\s)', n))
