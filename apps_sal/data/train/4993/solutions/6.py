from math import *
GRAVITY_ACC = 9.81 * 3.6 * 60.0
DRAG = 60.0 * 0.3 / 3.6
DELTA_T = 1.0 / 60.0
G_THRUST = 60 * 3.6 * 3.6
MASS = 80.0
WATTS0 = 225.0
D_WATTS = 0.5


def temps(v0, slope, d_tot):
    (t, d, v, watts) = (0, 0, v0, WATTS0)

    def nextAcc():
        a = -GRAVITY_ACC * slope / sqrt(10000 + slope ** 2) - DRAG * abs(v) ** 2 / MASS + G_THRUST * watts / (v * MASS)
        return a if abs(a) > 1e-05 else 0

    def nextVel():
        return v + gamma * DELTA_T

    def nextPow():
        return watts - D_WATTS * DELTA_T

    def nextDist():
        return d + v * DELTA_T / 60 + 0.5 * gamma * (DELTA_T / 60) ** 2

    def nextT():
        return t + DELTA_T
    gamma = nextAcc()
    while d_tot - d > 0 and v - 3.0 > 0.01:
        t = nextT()
        v = nextVel()
        watts = nextPow()
        gamma = nextAcc()
        d = nextDist()
    return -1 if v - 3.0 < 0.01 else int(round(t))
