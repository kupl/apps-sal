def bar_triang(pointA, pointB, pointC):
    (xa, ya) = pointA
    (xb, yb) = pointB
    (xc, yc) = pointC
    xO = round((xa + xb + xc) / 3, 4)
    yO = round((ya + yb + yc) / 3, 4)
    return [xO, yO]
