from math import sin, cos, pi

def crusoe(n, d, ang, dist_mult, ang_mult):
    x = y = z = 0.0
    for i in range(n):
        z = ang * pi / 180
        x += d * cos(z)
        y += d * sin(z)
        d *= dist_mult
        ang *= ang_mult
    return x, y
