def find_slope(points):
    (a, b, c, d) = points
    return str((b - d) // (a - c)) if a != c else 'undefined'
