def find_slope(points):
    (a, b, c, d) = points
    if a == c:
        return 'undefined'
    else:
        return str((d - b) // (c - a))
