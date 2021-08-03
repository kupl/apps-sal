import math


def tankvol(h, d, vt):
    r = d / 2.0
    if h == r:
        return vt / 2     # is the tank half full?
    half = h > r                 # is it more than half full
    h = d - h if half else h     # adjust h accordingly
    a = r - h                    # perpendicular intercept of the chord
    b = math.sqrt(r**2 - a**2)   # half the chord
    t = 2 * math.asin(b / r)       # the angle the chord sweeps out
    A = r**2 * t / 2 - b * a         # the area of the segment
    v = vt * A / (math.pi * r**2)    # the volume of the segment
    return int(vt - v) if half else int(v)
