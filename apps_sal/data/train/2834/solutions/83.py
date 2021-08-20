def symmetric_point(p, q):
    reflected_x = q[0] + (q[0] - p[0])
    try:
        slope = (q[1] - p[1]) / (q[0] - p[0])
        b = p[1] - slope * p[0]
        reflected_y = slope * reflected_x + b
    except ZeroDivisionError:
        reflected_y = p[1]
    return [round(reflected_x), round(reflected_y)]
