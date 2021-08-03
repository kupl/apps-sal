def dithering(width, height, x=0, y=0, c=1):
    if width <= c and height <= c:
        if x < width and y < height:
            yield (x, y)
        return
    for u, v in (x, y), (x + c, y + c), (x + c, y), (x, y + c):
        for p, q in dithering(width, height, u, v, c + c):
            yield p, q
