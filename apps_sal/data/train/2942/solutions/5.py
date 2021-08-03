from math import ceil, log2


def fold_to(distance, thickness=1e-4):
    if distance >= 0:
        return distance >= thickness and ceil(log2(distance / thickness))
