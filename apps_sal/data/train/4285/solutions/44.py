def find_slope(points):
    delta_x = points[0] - points[2]
    delta_y = points[1] - points[3]
    return str(delta_y // delta_x) if delta_x else 'undefined'

