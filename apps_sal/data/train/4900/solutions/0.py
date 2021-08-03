import math


def f(z, eps):
    if (abs(z) >= 1.0):
        return -1
    return int(math.log(eps) / math.log(abs(z)))
