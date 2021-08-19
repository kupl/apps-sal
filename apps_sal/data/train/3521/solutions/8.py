def on_line(points):
    try:
        (x1, y1) = points[0]
        (x2, y2) = points[-1]
    except:
        return True
    for i in points[1:-1]:
        (x3, y3) = i
        if (x1 - x3) * (y2 - y3) != (x2 - x3) * (y1 - y3):
            return False
    return True
