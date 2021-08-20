import math


def squares_needed(grains):
    return 0 if grains == 0 else 1 + math.floor(math.log2(grains))
