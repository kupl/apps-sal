from math import ceil, floor


def round_it(n):
    s = str(n).split('.')
    if len(s[0]) < len(s[1]):
        return ceil(n)
    if len(s[0]) > len(s[1]):
        return floor(n)
    return round(n)
