from math import ceil


def round_it(n):
    x = str(n).split('.')
    if len(x[0]) < len(x[1]):
        return ceil(n)
    if len(x[0]) > len(x[1]):
        return int(n)
    return round(n, 0)
