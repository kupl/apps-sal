from math import pi


def iter_pi(epsilon):
    sum, n = 0, 0
    while abs(4 * sum - pi) > epsilon:
        sum += ((-1)**n) / (2 * n + 1)
        n += 1
    return [n, round(4 * sum, 10)]
