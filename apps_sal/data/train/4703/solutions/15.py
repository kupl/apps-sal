def bar_triang(pointA, pointB, pointC):
    xO = '{:.4f}'.format(float(pointA[0] + pointB[0] + pointC[0]) / 3)
    yO = '{:.4f}'.format(float(pointA[1] + pointB[1] + pointC[1]) / 3)
    return [float(xO), float(yO)]
