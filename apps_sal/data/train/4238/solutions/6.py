from math import log2


def squares_needed(grains):
    return int(log2(grains)) + 1 if grains else 0
