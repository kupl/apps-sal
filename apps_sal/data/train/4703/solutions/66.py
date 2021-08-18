def bar_triang(pointA, pointB, pointC):
    return [round((pointA[i] + pointB[i] + pointC[i]) / 3, 4) for i in range(2)]
