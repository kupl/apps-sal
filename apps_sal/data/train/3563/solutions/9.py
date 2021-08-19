from math import ceil


def distance(n):
    m = ceil((n ** 0.5 - 1) / 2)
    x = y = m
    t = 1 + 4 * m * (m + 1)
    for (dx, dy) in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        if n == t:
            break
        d = min(t - n, 2 * m)
        x += dx * d
        y += dy * d
        t -= d
    return abs(x) + abs(y)
