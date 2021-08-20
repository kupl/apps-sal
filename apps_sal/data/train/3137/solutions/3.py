from math import ceil


def round_it(n):
    (a, b) = map(len, str(n).split('.'))
    if a > b:
        return int(n)
    if b > a:
        return ceil(n)
    return round(n)
