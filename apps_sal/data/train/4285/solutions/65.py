def find_slope(points):
    a, b, c, d = points
    try:
        return str(int((d - b) / (c - a)))
    except ZeroDivisionError:
        return 'undefined'
