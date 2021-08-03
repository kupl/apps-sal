from math import log


def f(z, eps):
    return int(log(eps) / log(abs(z))) if abs(z) < 1 else -1
