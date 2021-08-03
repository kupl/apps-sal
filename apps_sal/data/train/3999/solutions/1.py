from math import pi


def cup_volume(d1, d2, height):
    r1, r2 = d1 / 2.0, d2 / 2.0
    return round(pi * height * (pow(r1, 2) + r1 * r2 + pow(r2, 2)) / 3.0, 2)
