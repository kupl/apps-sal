import math


def squares_needed(grains):
    if grains == 0:
        return 0
    if grains == 1:
        return 1
    res = math.floor(math.log(grains, 2)) + 1
    return res
