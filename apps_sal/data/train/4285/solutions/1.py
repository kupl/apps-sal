def find_slope(points):
    (x1, y1, x2, y2) = points
    dx = x2 - x1
    dy = y2 - y1
    if dx != 0:
        return str(int(dy / dx))
    else:
        return 'undefined'
