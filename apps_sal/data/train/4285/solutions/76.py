def find_slope(points):
    return(str(int((points[3] - points[1])/(points[2] - points[0]))) if points[0] != points[2] else "undefined")
