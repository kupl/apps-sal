from math import atan, sin
GRAVITY_ACC = 9.81 * 3.6 * 60.0
DRAG = 60.0 * 0.3 / 3.6
DELTA_T = 1.0 / 60.0
G_THRUST = 60 * 3.6 * 3.6
MASS = 80.0
WATTS0 = 225.0
D_WATTS = 0.5


def temps(v0, slope, d_tot):
    t = 0
    v = v0
    d = 0
    watts = WATTS0
    theta = atan(slope / 100)
    while d < d_tot:
        t += DELTA_T
        watts -= D_WATTS * DELTA_T
        gamma = G_THRUST * watts / (v * MASS)
        gamma -= GRAVITY_ACC * sin(theta)
        gamma -= DRAG * v * v / MASS
        v += gamma * DELTA_T
        if v - 3 <= 0.01:
            return -1
        d += v * DELTA_T / 60
    return round(t)
