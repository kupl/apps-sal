import math
def squares_needed(grains):
    return grains if grains < 3 else math.ceil(math.log(grains+1,2))
