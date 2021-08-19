import math


def race(v1, v2, g):
    if v2 < v1:
        return None
    seconds = 0.1
    while v1 / 3600 * seconds + g >= v2 / 3600 * seconds:
        seconds += 0.05
    hours = seconds / 3600
    hoursRest = seconds % 3600
    minutes = hoursRest / 60
    seconds = hoursRest % 60
    return [math.floor(hours), math.floor(minutes), math.floor(seconds)]
