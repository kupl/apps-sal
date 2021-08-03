from re import fullmatch


def is_digit(n):
    return True if fullmatch(r'\d', n) else False
