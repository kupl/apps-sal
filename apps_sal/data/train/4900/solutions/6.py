from math import *


def f(z, eps):
    (x, y) = (z.real, z.imag)
    return max(-1, log(eps) / log(hypot(x, y)))
