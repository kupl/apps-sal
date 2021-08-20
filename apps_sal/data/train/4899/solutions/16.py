import math


def weight(n, w):
    i0 = (1 - 3 * math.exp(-2)) / 4
    iScale = [math.exp(-2 * k) for k in range(n + 1)]
    return w * i0 * sum(iScale)
