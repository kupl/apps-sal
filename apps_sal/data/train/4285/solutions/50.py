def find_slope(points):
    a, b, c, d = points[0], points[1], points[2], points[3]
    if a==c:
        return "undefined"
    else:
        return str(int((b-d)/(a-c)))
