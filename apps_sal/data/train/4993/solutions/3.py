import math


GRAVITY_ACC = 9.81 * 3.6 * 60.0  # gravity acceleration
DRAG = 60.0 * 0.3 / 3.6  # force applied by air on the cyclist
DELTA_T = 1.0 / 60.0  # in minutes
G_THRUST = 60 * 3.6 * 3.6  # pedaling thrust
MASS = 80.0  # biker's mass
WATTS0 = 225.0  # initial biker's power
D_WATTS = 0.5  # loss of power at each deltaT


def temps(v0, slope, d_tot):
    t = 0  # time
    gamma = 0  # total acceleration with its 3 components
    v = v0  # speed
    d = 0  # distance travelled
    watts = WATTS0  # biker's power

    # angle of inclination
    alpha = math.atan(slope / 100.0)

    while d < d_tot:
        if v - 3.0 <= 0.01:
            return -1
        t += DELTA_T
        watts -= D_WATTS * DELTA_T
        gamma = (-GRAVITY_ACC * math.sin(alpha)) + (-DRAG * abs(v) * abs(v) / MASS)
        if watts > 0 and v > 0:
            gamma += (G_THRUST * watts / (v * MASS))
        if abs(gamma) <= 0.00001:
            gamma = 0.0

        v += (gamma * DELTA_T)
        d += (v * DELTA_T / 60.0)

    return round(t)
