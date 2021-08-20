def find_slope(points):
    (x1, y1, x2, y2) = points[:]
    slope = (y1 - y2) // (x1 - x2) if x1 != x2 else 'undefined'
    return str(slope)
