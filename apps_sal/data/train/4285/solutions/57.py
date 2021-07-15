def find_slope(points):
    if points[0] != points[2]:
        return str(int((points[3]-points[1]) / (points[2]-points[0])))
    else:
        return "undefined"
