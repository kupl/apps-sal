from math import ceil


def get_participants(hs):
    return ceil((1 + (1 + 8 * hs) ** 0.5) / 2)
