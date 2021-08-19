def find_slope(points):
    dx = points[2] - points[0]
    dy = points[3] - points[1]
    try:
        m = dy / dx
        return f'{int(m)}'
    except:
        return 'undefined'
