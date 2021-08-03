def fold_to(distance):
    from math import log, ceil
    distance = float(distance)
    paper = 0.0001
    if distance >= paper:
        return ceil(log(distance / paper, 2))
    else:
        if distance >= 0:
            return 0
        else:
            return None
