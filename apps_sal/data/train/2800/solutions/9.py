from math import cos, pi, sin
SHIP_MPH = 90
NET_LENGTH = 40


def find_time_to_break(bearing_A, bearing_B):
    (ba, bb) = (bearing_A + 360, bearing_B + 360)
    alpha = min(abs(ba - bb), abs(bb - ba))
    if alpha > 180:
        alpha = 360 - alpha
    if alpha == 0:
        return float('inf')
    theta = alpha / 2 / 180 * pi
    s1 = (SHIP_MPH * sin(theta), SHIP_MPH * cos(theta))
    s2 = (SHIP_MPH * sin(-theta), SHIP_MPH * cos(-theta))
    mph = ((s1[0] - s2[0]) ** 2 + (s1[1] - s2[1]) ** 2) ** 0.5
    return NET_LENGTH / mph * 60
