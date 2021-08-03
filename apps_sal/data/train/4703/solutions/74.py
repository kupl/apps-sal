def bar_triang(pointA, pointB, pointC):

    x0 = (pointA[0] + pointB[0] + pointC[0]) / 3

    y0 = (pointA[1] + pointB[1] + pointC[1]) / 3

    return [round(x0, 4), round(y0, 4)]
