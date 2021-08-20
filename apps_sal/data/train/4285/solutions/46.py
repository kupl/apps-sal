def find_slope(points):
    return 'undefined' if points[0] == points[2] else str(round((points[3] - points[1]) / (points[2] - points[0])))
