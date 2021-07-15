from math import ceil, floor, sqrt


def triangular(n):
    return n * (n + 1) / 2


def quadratic_root(t):
    return (-1 + sqrt(1 + 8 * t)) / 2


def triangular_range(start, stop):
    first = int(ceil(quadratic_root(start)))
    last = int(floor(quadratic_root(stop)))

    result = {}
    t = triangular(first)
    for n in range(first, last + 1):
        result[n] = t
        t += n + 1

    return result

