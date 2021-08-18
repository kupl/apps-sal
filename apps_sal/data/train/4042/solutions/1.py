from math import floor, sqrt


def points(n):
    A001182 = sum(floor(sqrt(n**2 - k**2)) for k in range(1, n))
    A000603 = A001182 + 2 * n + 1
    A000328 = 4 * A000603 - (4 * n + 3)
    return A000328
