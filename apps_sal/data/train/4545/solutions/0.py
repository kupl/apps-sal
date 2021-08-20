from math import atan2, degrees


def get_score(x, y):
    (r, a) = ((x * x + y * y) ** 0.5, degrees(atan2(y, x)) + 9)
    t = str([6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10][int(a + 360 if a < 0 else a) // 18])
    for (l, s) in [(6.35, 'DB'), (15.9, 'SB'), (99, t), (107, 'T' + t), (162, t), (170, 'D' + t)]:
        if r <= l:
            return s
    return 'X'
