def find_slope(points):
    vertical_change = points[3] - points[1]
    horizontal_change = points[2] - points[0]
    try:
        slope = vertical_change / horizontal_change
    except ZeroDivisionError:
        return 'undefined'
    return str(int(slope))
