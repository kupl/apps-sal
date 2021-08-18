def bar_triang(pointA, pointB, pointC):
    x1, x2, x3 = pointA[0], pointB[0], pointC[0]
    y1, y2, y3 = pointA[1], pointB[1], pointC[1]
    return [round((x1 + x2 + x3) / 3, 4), round((y1 + y2 + y3) / 3, 4)]
