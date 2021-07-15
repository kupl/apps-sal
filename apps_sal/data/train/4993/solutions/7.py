import math
def temps(v0, slope, d_tot):
    time = 0
    gamma = 0
    v = v0
    d = 0
    watts = 225.0
    while True:
        gamma = 0
        if d >= d_tot:
            return round(time)
        if (v - 3.0) <= 0.01:
            return -1
        watts -= (0.5 * (1.0 / 60.0))
        angle = math.atan(slope / 100)
        gamma -= 9.81 * 3.6 * 60.0 * math.sin(angle)
        gamma -= (60.0 * 0.3 / 3.6) * abs(v) * abs(v) / 80.0
        if watts > 0 and v > 0:
            gamma += 60 * 3.6 * 3.6 * watts / (v * 80.0)
        if abs(gamma) <= 0.00001:
            gamma = 0
        v += (gamma * (1.0 / 60.0))
        d += (v * (1.0 / 60.0) / 60.0)
        time += (1.0 / 60.0)
