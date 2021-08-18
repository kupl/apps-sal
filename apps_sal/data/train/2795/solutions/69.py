from math import floor


def cockroach_speed(s):
    conversion = 1 / 27.7778
    cmPerSec = s / conversion
    return floor(cmPerSec)
