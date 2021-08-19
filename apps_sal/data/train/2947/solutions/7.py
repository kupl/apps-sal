from math import ceil, floor


def rounding(n, m):
    (a, b) = (m * ceil(n / m), m * floor(n / m))
    (da, db) = (abs(n - a), abs(n - b))
    if da == db:
        return n
    if da < db:
        return a
    return b
