from math import log


def fold_to(d):
    if d == 0:
        return 0
    if d > 0:
        a = (log(d / 0.0001) // log(2)) + 1
        return max(a, 0)
