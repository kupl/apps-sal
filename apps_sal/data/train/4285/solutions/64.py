def find_slope(points):
    x0, y0, x1, y1 = points[0], points[1], points[2], points[3]
    if x1 - x0 == 0:
        return "undefined"
    return str((y1 - y0) // (x1 - x0))
