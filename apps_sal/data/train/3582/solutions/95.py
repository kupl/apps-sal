from re import fullmatch


def is_digit(n):
    return True if fullmatch('\\d', n) else False
