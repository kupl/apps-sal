def bar_triang(pointA, pointB, pointC):
    xO = (pointA[0] + pointB[0] + pointC[0]) / 3
    yO = (pointA[1] + pointB[1] + pointC[1]) / 3
    xO = round(xO, 4)
    yO = round(yO, 4)
    return [xO, yO]
