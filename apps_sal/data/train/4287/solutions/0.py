from math import ceil


def get_participants(h):
    return int(ceil(0.5 + (0.25 + 2 * h) ** 0.5))
