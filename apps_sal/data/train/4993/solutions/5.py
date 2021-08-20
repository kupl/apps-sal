import math


def temps(v0, slope, d_tot):
    GRAVITY_ACC = 9.81 * 3.6 * 60.0
    DRAG = 60.0 * 0.3 / 3.6
    DELTA_T = 1.0 / 60.0
    G_THRUST = 60 * 3.6 * 3.6
    MASS = 80.0
    WATTS0 = 225.0
    D_WATTS = 0.5
    t = 0
    gamma = 0
    v = v0
    d = 0
    watts = WATTS0
    w = wei(slope, MASS)
    while d < d_tot:
        t += DELTA_T
        watts = watts - D_WATTS * DELTA_T
        grav = GRAVITY_ACC * w
        drag = DRAG * v * v / MASS
        gamma = -grav - drag
        if watts > 0 < v:
            gamma += G_THRUST * watts / (v * MASS)
        if abs(gamma) <= 1e-05:
            gamma = 0
        v = v + gamma * DELTA_T
        d = d + v * DELTA_T / 60
        if v - 3 <= 0.01:
            return -1
    return round(t)


def wei(slope, MASS):
    angle = math.atan(slope / 100)
    return math.sin(angle)
