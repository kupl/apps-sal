def find_slope(points):
    if points[0] - points[2] == 0:
        return 'undefined'
    else:
        return str(int((points[3] - points[1]) / (points[2] - points[0])))
