def find_slope(points):
    a, b, c, d = points
    if a - c == 0:
        return 'undefined'
    return str(int((b - d) / (a - c)))
