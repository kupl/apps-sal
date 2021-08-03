from math import ceil


def group_size(S, D):
    return ceil(((1 + 4 * (S**2 - S + 2 * D))**.5 - 1) / 2)
