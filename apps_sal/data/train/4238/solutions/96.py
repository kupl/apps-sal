from math import log, floor


def squares_needed(grains):
    if grains == 0:
        return 0
    return floor(log(grains, 2)) + 1
