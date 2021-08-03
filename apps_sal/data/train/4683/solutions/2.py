import itertools
from math import pi


def iter_pi(epsilon):
    sign = 1
    value = 4
    n = 1
    for i in itertools.count(1):
        if abs(value - pi) < epsilon:
            return [i, round(value, 10)]
        sign = -sign
        n += 2
        value += sign * (4 / n)
