def bar_triang(pointA, pointB, pointC):
    x1, y1 = pointA
    x2, y2 = pointB
    x3, y3 = pointC
    x0 = (x1 + x2 + x3) / 3
    y0 = (y1 + y2 + y3) / 3
    return [round(x0, 4), round(y0, 4)]
