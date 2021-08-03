from math import floor, ceil


def round_it(n):
    a, b = str(n).split('.')
    if len(a) > len(b):
        return floor(n)
    if len(a) < len(b):
        return ceil(n)
    return round(n)
