def squares_needed(grains):
    import math
    # base case
    if grains == 0:
        return 0
    elif grains == 1:
        return 1
    n = math.log(grains + 1, 2)
    return math.ceil(n)
