def find_slope(points):
    if points[2] == points[0]:
        return "undefined"
    a = int((points[3] - points[1]) / (points[2] - points[0]))
    print(a)
    return str(a)
