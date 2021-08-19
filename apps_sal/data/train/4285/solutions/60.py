def find_slope(points):
    try:
        return f'{int((points[3] - points[1]) / (points[2] - points[0]))}'
    except ZeroDivisionError:
        return 'undefined'
