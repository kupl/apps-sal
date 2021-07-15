from math import pi

def cup_volume(d1, d2, h):
    return round(h / 12.0 * pi * (d1**2 + d1*d2 + d2**2), 2)
