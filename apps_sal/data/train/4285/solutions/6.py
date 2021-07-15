def find_slope(points):
    delta_x = points[2] - points[0]
    delta_y = points[3] - points[1]
    if delta_x == 0:
        return "undefined"
    return str(delta_y // delta_x)
