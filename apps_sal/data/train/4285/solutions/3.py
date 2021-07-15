def find_slope(points):
    x1, y1, x2, y2 = points
    try:
        slope = f'{(y2 - y1) // (x2 - x1)}'
    except ZeroDivisionError as e:
        slope = 'undefined'
    return slope
