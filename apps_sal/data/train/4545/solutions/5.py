import math
(STR_MODIFIERS, STR_OUT) = ('TD', 'X')
PI = math.pi
(OUT_OF_BORDER, ANGLE_OFFSET) = (340.0 / 2, 2 * PI / 40)
CIRCLES = {(0, 12.7): 'DB', (12.7, 31.8): 'SB', (198, 214): 'T', (324, 340): 'D'}
PARTS = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]


def get_score(x, y):
    (ans, d) = ('', (x ** 2 + y ** 2) ** 0.5)
    theta = (math.atan(y / float(x)) + PI * (x < 0) + ANGLE_OFFSET + 2 * PI) % (2 * PI)
    if d > OUT_OF_BORDER:
        return STR_OUT
    for (k, v) in CIRCLES.items():
        if k[0] / 2.0 < d < k[1] / 2.0:
            if v not in STR_MODIFIERS:
                return v
            ans += v
            break
    return ans + str(PARTS[int(theta / (2 * PI / 20))])
