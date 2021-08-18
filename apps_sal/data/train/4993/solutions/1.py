from math import *

GRAVITY_ACC = 9.81 * 3.6 * 60.0
DRAG = 60.0 * 0.3 / 3.6
DELTA_T = 1.0 / 60.0
G_THRUST = 60 * 3.6 * 3.6
MASS = 80.0
WATTS0 = 225.0
D_WATTS = 0.5


def gamma(v, watts, slope):
    temp = -GRAVITY_ACC * sin(atan(0.01 * slope))
    temp = temp - DRAG * abs(v) * abs(v) / MASS
    temp = temp + G_THRUST * watts / (v * MASS)
    if abs(temp) <= 0.00001:
        temp = 0
    return temp


def temps(v0, slope, d_tot):
    d = 0
    t = 0
    v = v0
    watts = WATTS0

    while (d < d_tot):

        watts = watts - D_WATTS * DELTA_T
        v = v + gamma(v, watts, slope) * DELTA_T
        d = d + v * DELTA_T / 60
        t = t + DELTA_T
        if v - 3.0 <= 0.01:
            return -1

    return round(t)
