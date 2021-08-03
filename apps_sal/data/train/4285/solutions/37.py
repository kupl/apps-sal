def find_slope(points):
    rise = points[3] - points[1]
    run = points[2] - points[0]
    return str(rise // run) if run else 'undefined'
