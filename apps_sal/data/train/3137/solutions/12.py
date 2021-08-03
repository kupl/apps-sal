from math import ceil, floor


def round_it(n):
    t = str(n).split('.')
    t = [len(x) for x in t]
    return ceil(n) if t[0] < t[1] else floor(n) if t[0] > t[1] else round(n)
