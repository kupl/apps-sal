def find_slope(points):
    side1 = points[2] - points[0]
    side2 = points[3] - points[1]
    return str(side2//side1) if side1 != 0 else "undefined"

