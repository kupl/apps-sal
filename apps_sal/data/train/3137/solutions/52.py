from math import ceil, floor


def round_it(n):
    s = str(n)
    if s.index('.') * 2 < len(s) - 1:
        return ceil(n)
    elif s.index('.') * 2 > len(s) - 1:
        return floor(n)
    else:
        return round(n)
