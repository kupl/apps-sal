from math import hypot, atan2, degrees


def get_score(x, y):
    r = hypot(x, y)
    fi = degrees(atan2(y, x))
    dictio = {-9 < fi < 9: '6', 9 < fi < 27: '13', 27 < fi < 45: '4', 45 < fi < 63: '18', 63 < fi < 81: '1', 81 < fi < 99: '20', 99 < fi < 117: '5', 117 < fi < 135: '12', 135 < fi < 153: '9', 153 < fi < 171: '14', -27 < fi < -9: '10', -45 < fi < -27: '15', -63 < fi < -45: '2', -81 < fi < -63: '17', -99 < fi < -81: '3', -117 < fi < -99: '19', -135 < fi < -117: '7', -153 < fi < -135: '16', -171 < fi < -153: '8', -180 < fi < -171: '11', 171 < fi < 180: '11'}
    if r > 170:
        return 'X'
    if 0 <= r <= 6.35:
        return 'DB'
    if 6.35 < r <= 15.9:
        return 'SB'
    number = dictio[True]
    return 'T' * (99 < r < 107) + 'D' * (162 < r < 170) + number
