def squares_needed(g):
    r = 0
    while g >= 2:
        g = g >> 1
        r += 1

    return r + (g != 0)
