import math


def count_black_cells(h, w):
    r, y, up, t = 0, 1, 0, None
    while(y <= w):
        t = math.ceil(h * y / w)
        r += t - up + (1 if y != w and h * y / w == t else 0)
        y += 1
        up = t - 1
    return r
