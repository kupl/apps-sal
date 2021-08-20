from math import sin, atan


def temps(v0, slope, d_tot):
    GRAVITY_ACC = 9.81 * 3.6 * 60.0
    DRAG = 60.0 * 0.3 / 3.6
    DELTA_T = 1.0 / 60.0
    D_WATTS = 0.5
    G_THRUST = 60 * 3.6 * 3.6
    MASS = 80
    WATTS0 = 225
    t = 0.0
    d = 0.0
    v = v0
    gamma = 0.0
    watts = WATTS0
    slopeGravityAcc = -GRAVITY_ACC * sin(atan(slope / 100.0))
    while d <= d_tot:
        t += DELTA_T
        watts -= D_WATTS * DELTA_T
        gamma = slopeGravityAcc - DRAG * abs(v) * abs(v) / MASS
        if watts > 0.0 and v > 0.0:
            gamma += G_THRUST * watts / (v * MASS)
        if abs(gamma) <= 1e-05:
            gamma = 0.0
        else:
            v += gamma * DELTA_T
        d += v * DELTA_T / 60.0
        if v - 3.0 <= 0.01:
            return -1
    return round(t)
