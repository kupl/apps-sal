def find_slope(points):
    (x1, y1, x2, y2) = (points[0], points[1], points[2], points[3])
    if x1 == x2:
        return 'undefined'
    else:
        return str(int((y1 - y2) / (x1 - x2)))
