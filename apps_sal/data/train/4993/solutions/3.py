import math
GRAVITY_ACC = 9.81 * 3.6 * 60.0
DRAG = 60.0 * 0.3 / 3.6
DELTA_T = 1.0 / 60.0
G_THRUST = 60 * 3.6 * 3.6
MASS = 80.0
WATTS0 = 225.0
D_WATTS = 0.5


def temps(v0, slope, d_tot):
    t = 0
    gamma = 0
    v = v0
    d = 0
    watts = WATTS0
    alpha = math.atan(slope / 100.0)
    while d < d_tot:
        if v - 3.0 <= 0.01:
            return -1
        t += DELTA_T
        watts -= D_WATTS * DELTA_T
        gamma = -GRAVITY_ACC * math.sin(alpha) + -DRAG * abs(v) * abs(v) / MASS
        if watts > 0 and v > 0:
            gamma += G_THRUST * watts / (v * MASS)
        if abs(gamma) <= 1e-05:
            gamma = 0.0
        v += gamma * DELTA_T
        d += v * DELTA_T / 60.0
    return round(t)
