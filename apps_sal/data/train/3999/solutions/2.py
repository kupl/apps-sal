from math import pi

def cup_volume(d1, d2, h):
    return round(pi * h * (d1**2 + d1 * d2 + d2**2) / 12, 2)
