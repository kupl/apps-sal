def bar_triang(pointA, pointB, pointC):
    x = sum([pointA[0], pointB[0], pointC[0]]) / 3.0
    y = sum([pointA[1], pointB[1], pointC[1]]) / 3.0
    return [round(x, 4), round(y, 4)]
