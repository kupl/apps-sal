from math import ceil, floor


def round_it(n):
    a, b = map(len, str(n).split('.'))
    if a < b:
        return ceil(n)
    if a > b:
        return floor(n)
    return round(n)
