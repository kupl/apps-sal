import math


def squares_needed(grains):
    if grains == 0:
        return 0
    a = math.ceil(math.log(grains + 1, 2))
    return a
