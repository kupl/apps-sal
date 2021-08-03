import math


def roots(a, b, c):
    dis = b ** 2 - 4 * a * c
    if dis < 0:
        return None
    return round(((-b + math.sqrt(dis)) / (2 * a)) + ((-b - math.sqrt(dis)) / (2 * a)), 2)
