from math import ceil, log2


def fold_to(distance):
    thickness = 0.0001
    if distance < 0:
        return None
    if distance <= thickness:
        return 0
    return ceil(log2(distance / thickness))
