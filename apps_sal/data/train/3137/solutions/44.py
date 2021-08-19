from math import ceil, floor


def round_it(n):
    (l, r) = str(n).split('.')
    if len(l) > len(r):
        return floor(n)
    elif len(l) < len(r):
        return ceil(n)
    else:
        return round(n)
