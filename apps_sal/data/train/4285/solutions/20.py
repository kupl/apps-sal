def find_slope(points):
    return str(int((points[1] - points[3]) / (points[0] - points[2])))if len(points) == 4 and (points[0] - points[2]) != 0 else 'undefined'
