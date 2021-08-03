from math import pi


def cup_volume(d1, d2, h):
    r1, r2 = d1 / 2, d2 / 2
    return round(pi * (1 / 3) * h * (r1**2 + r2**2 + r1 * r2), 2)
