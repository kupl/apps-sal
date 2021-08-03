def bar_triang(pointA, pointB, pointC):
    x_bary = round((pointA[0] + pointB[0] + pointC[0]) / 3, 4)
    y_bary = round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)
    return [x_bary, y_bary]
