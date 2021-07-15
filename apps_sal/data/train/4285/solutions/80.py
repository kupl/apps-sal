def find_slope(points):
    try:
        return str(int((points[1] - points[3]) / (points[0] - points[2])))
    except:
        return "undefined"
