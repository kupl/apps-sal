import math


def cockroach_speed(s):

    cm = 100000
    sec = 3600
    s = math.floor(s * (cm / sec))
    return s
