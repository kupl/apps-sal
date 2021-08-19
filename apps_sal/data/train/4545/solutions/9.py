from math import atan, pi


def get_score(x, y):
    d = (x * x + y * y) ** 0.5
    if d < 6.35:
        return 'DB'
    if d < 15.9:
        return 'SB'
    if 170 < d:
        return 'X'
    prefix = 'D' if 162 < d else 'T' if 99 < d < 107 else ''
    slice = round((atan(y / x) / pi + (x < 0)) * 10) % 20
    return prefix + '6 13 4 18 1 20 5 12 9 14 11 8 16 7 19 3 17 2 15 10'.split()[slice]
