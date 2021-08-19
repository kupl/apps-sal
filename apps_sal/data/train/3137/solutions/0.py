from math import ceil


def round_it(n):
    (left, right) = (len(part) for part in str(n).split('.'))
    return ceil(n) if left < right else int(n) if left > right else round(n)
