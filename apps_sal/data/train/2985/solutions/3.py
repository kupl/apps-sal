from math import gcd


def reflections(max_x, max_y):
    d = gcd(max_x, max_y)
    return max_x // d & max_y // d & 1
