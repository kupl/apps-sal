def find_slope(points):
    if points[2] - points[0] == 0:
        return "undefined"
    else:
        sloope = (points[3] - points[1]) // (points[2] - points[0])
        return str(sloope)
