import math


def not_visible_cubes(n):
    if (n < 2):
        return 0
    else:
        return (n - 2) * (n - 2) * (n - 2)
