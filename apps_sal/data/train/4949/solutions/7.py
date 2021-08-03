from math import cos, sin, pi


def crusoe(n, d, ang, dist_mult, ang_mult):
    x, y = 0, 0
    for i in range(n):
        x += cos(ang * pi / 180) * d
        y += sin(ang * pi / 180) * d
        ang *= ang_mult
        d *= dist_mult
    return [x, y]
