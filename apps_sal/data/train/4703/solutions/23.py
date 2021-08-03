def bar_triang(pointA, pointB, pointC):
    x_0 = round((pointA[0] + pointB[0] + pointC[0]) / 3, 4)
    y_0 = round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)
    return [x_0, y_0]
