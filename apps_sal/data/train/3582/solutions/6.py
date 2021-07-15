def is_digit(n):
    from re import search
    return bool(search('\A\d\Z', n))
