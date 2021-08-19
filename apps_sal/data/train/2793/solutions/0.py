from math import floor


def group_size(S, D):
    return floor((2 * D + S * (S - 1)) ** 0.5 + 0.5)
