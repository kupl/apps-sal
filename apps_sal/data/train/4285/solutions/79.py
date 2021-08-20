def find_slope(points):
    (a, b, c, d) = points
    return str((d - b) // (c - a)) if a != c else 'undefined'
