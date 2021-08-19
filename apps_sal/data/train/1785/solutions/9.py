import math


def dithering(width, height):
    d = int(math.pow(2, math.ceil(math.log(max(width, height), 2))))
    return ((x, y) for (x, y) in _dithering(d) if x < width and y < height)


def _dithering(d):
    if d == 1:
        yield (0, 0)
        return
    fac = d // 2
    for (x, y) in _dithering(d >> 1):
        yield (x, y)
        yield (x + fac, y + fac)
        yield (x + fac, y)
        yield (x, y + fac)
