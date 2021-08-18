from math import cos, sin, pi


def crusoe(n, d, ang, dis_tmult, ang_mult):
    lastx = 0
    lasty = 0
    for i in range(n):
        lastx += d * cos((ang * ang_mult**i) * pi / 180) * dis_tmult**i
        lasty += d * sin((ang * ang_mult**i) * pi / 180) * dis_tmult**i
    return (lastx, lasty)
