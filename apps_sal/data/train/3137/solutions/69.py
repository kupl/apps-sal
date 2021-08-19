from math import ceil, floor


def round_it(n):
    l = str(n).split('.')
    if len(l[0]) == len(l[1]):
        return round(n)
    if len(l[0]) > len(l[1]):
        return floor(n)
    if len(l[0]) < len(l[1]):
        return ceil(n)
