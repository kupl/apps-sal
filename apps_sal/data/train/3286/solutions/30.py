def enough(c, o, w):
    return 0 if c - o >= w else w - (c - o)
