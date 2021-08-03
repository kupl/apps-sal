from math import sin, cos, pi


def crusoe(n, d, ang, dis_tmult, ang_mult):
    x = 0
    y = 0
    for i in range(n):

        x += d * cos((ang / 180) * pi)
        y += d * sin((ang / 180) * pi)
        d = d * dis_tmult
        ang = ang * ang_mult

    return (x, y)
