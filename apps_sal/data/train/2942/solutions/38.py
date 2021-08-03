from math import log, ceil


def fold_to(d):
    if d < 0:
        return None
    if d == 0:
        return 0
    return max(0, ceil(log(d / 0.0001, 2)))
