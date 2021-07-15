def isValid(f):
    a, b, c, d, e, f, g, h = [v in f for v in range(1, 9)]
    return not(a and b) and not(c and d) and not (e ^ f) and (g or h)

