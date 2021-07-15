def find_slope(points):
    try:
        k = (points[3] - points[1]) // (points[2] - points[0])
        return str(k)
    except ZeroDivisionError:
        return 'undefined'
