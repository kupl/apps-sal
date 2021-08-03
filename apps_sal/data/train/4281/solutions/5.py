import math


def tankvol(h, d, vt):
    return math.floor((d * d / 4 * math.acos(1 - (h / (d / 2))) - (math.sqrt(d * d / 4 - (d / 2 - h)**2) * (d / 2 - h))) * vt / (math.pi * d**2 / 4))
