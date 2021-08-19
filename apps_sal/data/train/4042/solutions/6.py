from math import sqrt


def points(n):
    return sum((int(sqrt(n ** 2 - i ** 2)) for i in range(n))) * 4 + 1
