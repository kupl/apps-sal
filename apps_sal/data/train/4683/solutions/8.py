import math


def iter_pi(epsilon):
    (pi, k) = (0, 0)
    while abs(pi - math.pi / 4) > epsilon / 4:
        pi += (-1) ** k * 1 / (2 * k + 1)
        k += 1
    pi *= 4
    return [k, round(pi, 10)]
