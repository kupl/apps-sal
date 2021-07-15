from math import cos, sin, pi
def crusoe(n, d, ang, dist_mult, ang_mult):
    def sim(center, scale, ang):
        resx = center[0] + scale * cos(ang * pi / 180.0)
        resy = center[1] + scale * sin(ang * pi / 180.0)
        return resx, resy
    center = (0.0, 0.0)
    for i in range(1, n + 1):
        center = sim(center, d, ang)
        d *= dist_mult
        ang *= ang_mult
    return center
