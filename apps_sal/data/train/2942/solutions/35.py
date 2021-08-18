def fold_to(distance):
    import math
    thick = 0.0001
    if distance < 0:
        return None
    elif distance < thick:
        return 0
    else:
        return math.ceil(math.log2(distance / thick))
