from itertools import cycle
from math import log2, ceil


def dithering(h, w):

    def rec(x, y, d, sendIt=True):
        d >>= 1
        if d:
            for g in cycle((rec(x + d * dx, y + d * dy, d, i) for (i, (dx, dy)) in enumerate([(0, 0), (1, 1), (1, 0), (0, 1)]))):
                yield next(g)
        else:
            yield (x, y)
    for (x, y) in rec(0, 0, 2 ** ceil(log2(max(w, h)))):
        if 0 <= x < h and 0 <= y < w:
            yield (x, y)
