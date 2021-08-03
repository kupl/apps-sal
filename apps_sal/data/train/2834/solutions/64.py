def symmetric_point(p, q):
    x1, y1 = p
    p1, p2 = q

    x2 = p1 * 2 - x1
    y2 = p2 * 2 - y1
    return [x2, y2]
