from math import atan, sin


def temps(v, slope, d_tot):
    answer = 0
    travelled = 0
    mass = 80
    power = 225
    power_loss = 0.5 / 60
    angle = atan(slope / 100)
    gravity_acc = 9.81 * 3.6 * 60
    gravityParallel = gravity_acc * sin(angle)
    drag = 60 * 0.3 / 3.6
    g_thrust = 60 * 3.6 * 3.6
    while travelled < d_tot:
        answer += 1
        airDrag = drag * v * v / mass
        thrust = 0
        if power > 0 and v > 0:
            thrust = g_thrust * power / v / mass
        gamma = -gravityParallel - airDrag + thrust
        if abs(gamma) <= 1e-05:
            gamma = 0
        v += gamma / 60
        if v - 3 <= 0.01:
            return -1
        travelled += v / 60 / 60
        power -= power_loss
    return round(answer / 60)
