def find_slope(points):
    (x1, y1, x2, y2) = points
    (dy, dx) = (y2 - y1, x2 - x1)
    return 'undefined' if dx is 0 else str(int(dy / dx))
