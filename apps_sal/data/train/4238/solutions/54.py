from math import log2


def squares_needed(grains):
    if grains == 0:
        return 0
    return int(log2(grains)) + 1
