def find_slope(points):
    (x1, y1, x2, y2) = points
    return f'{(y2 - y1) // (x2 - x1)}' if x1 != x2 else 'undefined'
