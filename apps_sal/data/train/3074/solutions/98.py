def growing_plant(u, d, h):
    v = 0
    for i in range(1, int(1000.0)):
        v += u
        if v >= h:
            return i
        else:
            v -= d
