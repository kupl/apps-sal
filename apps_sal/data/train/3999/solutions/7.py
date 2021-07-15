import math
def cup_volume(d1, d2, height):
    return round(math.pi * height * (d1**2 + d2**2 + d1*d2)/12, 2)
