def find_slope(points):
    a, b, c, d = points
    if c != a:
        return str(int((d - b) / (c - a)))
    else:
        return 'undefined'
