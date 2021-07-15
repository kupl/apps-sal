import math

def cup_volume(d1, d2, height):
    if d1 > d2:
        d1, d2 = d2, d1
    if d1 == d2:
        return round((d1/2.0) ** 2 * math.pi * height, 2)
    x = (d1 * float(height)) / (d2 - d1)
    vol = (d2 / 2.0)**2*math.pi*(height+x) / 3.0 - (d1 / 2.0)**2*math.pi*x/3.0
    return round(vol, 2)

