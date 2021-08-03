def find_slope(points):
    if points[-2] == points[0]:
        return 'undefined'
    return str(int((points[-1] - points[1]) / (points[-2] - points[0])))
