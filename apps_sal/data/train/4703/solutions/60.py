def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    xo = round((pointA[0] + pointB[0] + pointC[0]) / 3, 4)
    yo = round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)
    return [xo, yo]
