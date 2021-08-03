import math


def cockroach_speed(s):
    seconds = 60 * 60
    cm = 1000 * 100
    new_speed = s * cm / seconds
    return math.floor(new_speed)
