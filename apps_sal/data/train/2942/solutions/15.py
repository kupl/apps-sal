from math import log2, ceil


def fold_to(distance):
    return None if distance < 0 else ceil(log2(max(distance * 10000.0, 1)))
