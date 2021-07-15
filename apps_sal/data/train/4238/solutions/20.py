def squares_needed(grains):
    import math
    try:
        x = math.log(grains)
        y = math.log(2)
        n = (x / y) + 1
    except ValueError:
        return 0
    return math.floor(n)
