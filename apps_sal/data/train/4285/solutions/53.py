def find_slope(points):
    try:
        print('points =', points)
        (x1, y1, x2, y2) = points
        slope = (y2 - y1) / (x2 - x1)
        return f'{slope:.0f}' if slope != 0 else '0'
    except (TypeError, ValueError, ZeroDivisionError):
        return 'undefined'
