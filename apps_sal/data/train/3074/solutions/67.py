def growing_plant(u, d, h):
    r, c = u, 1
    while r < h:
        r += u - d
        c += 1
    return c
