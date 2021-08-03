import math


def cockroach_speed(s):
    cms = (s / 3600) * 100000
    return(math.floor(cms))
