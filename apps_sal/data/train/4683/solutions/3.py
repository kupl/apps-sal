import math


def iter_pi(epsilon):
    (pi, iD, c, pos) = (4.0, 1.0, 1, False)
    while abs(pi - math.pi) > epsilon:
        iD += 2.0
        (pi, pos) = (4 * (pi / 4 + (1 / iD if pos else -1 / iD)), not pos)
        c += 1
    return [c, round(pi, 10)]
