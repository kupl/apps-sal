from math import floor, sqrt


def group_size(s, d):
    return floor(sqrt(2 * d + s * (s - 1)) + 0.5)
