def isValid(formula):
    (a, b, c, d, e, f, g, h) = (v in formula for v in range(1, 9))
    return not (a and b) and (not (c and d)) and e ^ f ^ 1 and (g or h)
