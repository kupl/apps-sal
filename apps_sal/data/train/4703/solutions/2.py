def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3.0, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3.0, 4)]
