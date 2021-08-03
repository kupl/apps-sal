from math import ceil, log10, pi, e


def count(n):
    return ceil(log10(2 * pi * n) / 2 + n * (log10(n / e)))
