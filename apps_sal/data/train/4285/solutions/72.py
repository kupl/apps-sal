def find_slope(points):
    (x1, y1, x2, y2) = points
    if x1 == x2:
        return 'undefined'
    else:
        return str((y2 - y1) // (x2 - x1))
