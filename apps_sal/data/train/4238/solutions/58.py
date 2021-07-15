import math

def squares_needed(grains):
    return grains and int(math.log(grains, 2) + 1)
