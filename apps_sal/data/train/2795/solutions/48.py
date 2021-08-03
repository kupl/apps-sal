from math import floor


def cockroach_speed(s):
    x = 27.7777777778  # 1 km per hour converted to cm per second
    return floor(s * x)
