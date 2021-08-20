def find_slope(points):
    (x1, y1) = (points[0], points[1])
    (x2, y2) = (points[2], points[3])
    return str(int((y2 - y1) / (x2 - x1))) if x2 - x1 != 0 else 'undefined'
