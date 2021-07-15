def find_slope(points):
    x = points[2] - points[0]
    y = points[3] - points[1]
    return f"{round(y/x)}" if x else "undefined"
