import math
def squares_needed(grains):
    return 0 if not grains else int(math.log(grains)/math.log(2) + 1)
