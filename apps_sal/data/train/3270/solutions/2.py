from math import sqrt


def is_square(n):
    return round(sqrt(n)) ** 2 == n


def closest_pair_tonum(lim):
    for i in range(lim - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            if is_square(i + j) and is_square(i - j):
                return (i, j)
