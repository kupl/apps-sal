def bar_triang(pointA, pointB, pointC):
    x0 = round((pointA[0] + pointB[0] + pointC[0]) / 3, 4)
    y0 = round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)
    return [x0, y0]
