def enough(c, n, w):
    x = w - (c - n)
    return x if x > 0 else 0
