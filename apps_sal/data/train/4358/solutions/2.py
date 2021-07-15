import math

def ellipse_contains_point(f0, f1, l, p): 
    calc_len = lambda f: math.hypot(*(f[a] - p[a] for a in 'xy'))
    return calc_len(f0) + calc_len(f1) <= l
