def dithering(width, height):

    def rec(v, x, y):
        if not (x < width and y < height):
            return
        if not (x + v < width or y + v < height):
            yield (x, y)
            return
        for k in rec(2 * v, x, y):
            yield k
        for k in rec(2 * v, x + v, y + v):
            yield k
        for k in rec(2 * v, x + v, y):
            yield k
        for k in rec(2 * v, x, y + v):
            yield k
    for k in rec(1, 0, 0):
        yield k
