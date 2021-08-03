import math


def half_life(q0, q1, t):
    return 1 / (math.log(q0 / q1) / (t * math.log(2)))
