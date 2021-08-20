def bar_triang(pointA, pointB, pointC):
    (xa, xb, xc) = (pointA[0], pointB[0], pointC[0])
    (ya, yb, yc) = (pointA[1], pointB[1], pointC[1])
    x = round((xa + xb + xc) / 3, 4)
    y = round((ya + yb + yc) / 3, 4)
    return [x, y]
