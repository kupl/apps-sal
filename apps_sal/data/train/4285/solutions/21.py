def find_slope(points):
    (x1, y1, x2, y2) = points
    return str((y2 - y1) // (x2 - x1)) if x2 != x1 else 'undefined'
