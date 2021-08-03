from math import ceil, floor


def round_it(n):
    a, b = str(n).split(".")
    l1, l2 = len(a), len(b)
    if l1 < l2:
        return ceil(n)
    elif l1 > l2:
        return floor(n)
    return round(n)
