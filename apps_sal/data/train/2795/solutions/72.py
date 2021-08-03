import math


def cockroach_speed(s):
    converted_speed = (s * 100000) / (3600)
    return math.floor(converted_speed)
