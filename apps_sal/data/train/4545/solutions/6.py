from math import atan2, hypot, pi
ZONES = ['6', '13', '4', '18', '1', '20', '5', '12', '9', '14', '11', '8', '16', '7', '19', '3', '17', '2', '15', '10']


def get_score(x, y):
    dist = hypot(x, y)
    if dist > 170:
        return 'X'
    if dist < 6.35:
        return 'DB'
    if dist < 15.9:
        return 'SB'
    angle = (atan2(y, x) + pi / 20) % (2 * pi)
    zone = ZONES[int(angle / pi * 10)]
    if 99 < dist < 107:
        return 'T' + zone
    if 162 < dist < 170:
        return 'D' + zone
    return zone
