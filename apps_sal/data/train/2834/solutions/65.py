def symmetric_point(p, q):
    x1, y1 = p
    x2, y2 = q
    return [x2 + x2 - x1, y2 + y2 - y1]
