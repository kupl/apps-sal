def symmetric_point(p, q):
    (x1, y1) = p
    (x2, y2) = q
    (x3, y3) = (x2 - x1 + x2, y2 - y1 + y2)
    return [x3, y3]
