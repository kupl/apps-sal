from itertools import cycle


def max_hexagon_beam(n: int, seq: tuple):
    q = cycle(seq)
    (sx, sy, sz) = ([0] * (2 * n - 1), [0] * (2 * n - 1), [0] * (2 * n - 1))
    for z in range(-(n - 1), n):
        xp = -(n - 1) if z >= 0 else -(n - 1) - z
        xk = n - 1 if z <= 0 else n - 1 - z
        for x in range(xp, xk + 1):
            y = -(z + x)
            v = next(q)
            sx[x + n - 1] += v
            sy[y + n - 1] += v
            sz[z + n - 1] += v
    return max(sz + sy + sx)
