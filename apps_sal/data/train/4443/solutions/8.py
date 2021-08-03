from itertools import count


def max_ball(v0):
    g = 9.81
    c = count(0, 0.1)
    hh = -0.1
    while True:
        t = next(c)
        h = v0 * 1000 / 3600 * t - 0.5 * g * t * t
        if h - hh > 0:
            hh = h
        else:
            return int(round(t * 10, 2)) - 1
