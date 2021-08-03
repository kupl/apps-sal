import math


def is_negative_zero(n):
    return math.atan2(-0.0, -0.0) == math.atan2(n, n)
