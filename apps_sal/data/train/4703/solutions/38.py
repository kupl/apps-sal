def bar_triang(pointA, pointB, pointC):
    x = (pointA[0] + pointB[0] + pointC[0]) / 3
    y = (pointA[1] + pointB[1] + pointC[1]) / 3
    return [round(x * 10000) / 10000, round(y * 10000) / 10000]
