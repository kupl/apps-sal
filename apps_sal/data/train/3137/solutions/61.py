from math import ceil, floor


def round_it(n):
    (l, r) = map(len, str(n).split('.'))
    return ceil(n) if l < r else floor(n) if l > r else round(n)
