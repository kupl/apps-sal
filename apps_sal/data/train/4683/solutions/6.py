from math import pi


def iter_pi(epsilon):
    res = 0
    i = 0
    while abs(pi - res) > epsilon:
        res += (-1) ** (i % 2) * 4 / (1 + 2 * i)
        i += 1
    return [i, round(res, 10)]
