from math import ceil


def round_to_next5(n):
    return 5 * round(ceil(float(n) / 5))
