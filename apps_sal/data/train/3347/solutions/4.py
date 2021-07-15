def minimum(a, x):
    r = a % x
    return r and min(r, x - r)
