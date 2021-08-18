def bar_triang(pointA, pointB, pointC):
    xO, yO = round((pointA[0] + pointB[0] + pointC[0]) / 3, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)
    return [xO, yO]
