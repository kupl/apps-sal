from math import log


def isPP(n, e=1e-12):
    for p in range(2, int(log(n, 2)) + 1):
        if int(n ** (1. / p) + e) ** p == n:
            return [int(n ** (1. / p) + e), p]
