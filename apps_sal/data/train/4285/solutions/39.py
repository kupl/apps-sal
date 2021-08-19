def find_slope(points):
    x = points[2] - points[0]
    y = points[3] - points[1]
    if x == 0:
        return 'undefined'
    else:
        return str(int(y / x))
