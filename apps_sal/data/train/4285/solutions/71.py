def find_slope(points):
    return str((points[1] - points[3]) // (points[0] - points[2])) if points[0] - points[2] else 'undefined'
