from math import cos, sin, radians


def crusoe(n, d, ang, dist_mult, ang_mult):
    x, y, theta, r = 0, 0, 1, 1
    for i in range(n):
        theta = ang * ang_mult**i
        r = d * dist_mult**i
        x += r * cos(radians(theta))
        y += r * sin(radians(theta))

    return (x, y)
