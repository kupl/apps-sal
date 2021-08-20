def find_slope(points):
    y = points[1] - points[3]
    x = points[0] - points[2]
    try:
        return str(int(y / x))
    except:
        return 'undefined'
