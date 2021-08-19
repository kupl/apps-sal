def find_slope(points):
    x = int(points[2] - points[0])
    y = int(points[3] - points[1])
    return str(int(y / x)) if x != 0 else 'undefined'
