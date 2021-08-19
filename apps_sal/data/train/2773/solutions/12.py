from math import ceil, log


def calculate_years(p, i, t, d):
    x = float(d) / p
    base = 1 + i * (1 - t)
    return ceil(log(x, base))
