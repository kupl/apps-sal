def find_slope(points):
    dx = points[2] - points[0]
    dy = points[3] - points[1]
    return str(dy // dx) if dx != 0 else "undefined"
