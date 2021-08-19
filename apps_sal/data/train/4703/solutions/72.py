def bar_triang(pointA, pointB, pointC):
    x0 = (float(pointA[0]) + float(pointB[0]) + float(pointC[0])) / 3
    y0 = (float(pointA[1]) + float(pointB[1]) + float(pointC[1])) / 3
    return [round(x0, 4), round(y0, 4)]
