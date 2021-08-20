import math


def tankvol(h, d, vt):
    l = vt / (math.pi * (d / 2) ** 2)
    r = d / 2
    partOne = r ** 2 * math.acos((r - h) / r)
    partTwo = (r - h) * math.sqrt(2 * r * h - h ** 2)
    vs = l * (partOne - partTwo)
    return math.floor(vs)
