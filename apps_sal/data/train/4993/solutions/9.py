import math


def temps(v0, slope, d_tot):
    GRAVITY_ACC = 9.81 * 60.0 * 3.6
    DRAG = 60.0 * 0.3 / 3.6
    DELTA_T = 1.0 / 60.0
    G_THRUST = 60 * 3.6 * 3.6
    MASS = 80.0
    WATTS0 = 225.0
    D_WATTS = 0.5
    DELTA_P = D_WATTS * DELTA_T
    SLOPE = math.sin(math.atan(slope / 100.0))
    p = WATTS0
    v = v0
    (a, d, t) = (0.0, 0.0, 0.0)
    while d < d_tot:
        t += DELTA_T
        p -= DELTA_P
        a = -GRAVITY_ACC * SLOPE - DRAG * v ** 2 / MASS
        if v > 0 and p > 0:
            a += p * G_THRUST / v / MASS
        if abs(a) <= 1e-05:
            a = 0
        v += a * DELTA_T
        if v - 3.0 < 0.01:
            return -1
        d += v * DELTA_T / 60
    return int(round(t, 0))
