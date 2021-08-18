from math import sqrt


def ellipse_contains_point(f0, f1, l, p):
    d1 = sqrt((f0['x'] - p['x'])**2 + (f0['y'] - p['y'])**2)
    d2 = sqrt((f1['x'] - p['x'])**2 + (f1['y'] - p['y'])**2)

    return d1 + d2 <= l
