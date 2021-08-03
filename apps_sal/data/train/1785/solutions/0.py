def dithering(width, height, x=0, y=0, c=1):
    if width <= c and height <= c:
        if x < width and y < height:
            yield x, y
        return
    for u, v in (0, 0), (c, c), (c, 0), (0, c):
        for p, q in dithering(width, height, x + u, y + v, c + c):
            yield p, q
