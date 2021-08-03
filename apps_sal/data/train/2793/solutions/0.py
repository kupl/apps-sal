from math import floor


def group_size(S, D):
    return floor((2 * D + S * (S - 1))**.5 + .5)
