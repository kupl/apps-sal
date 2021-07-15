def bar_triang(pointA, pointB, pointC): 
    a = (pointA[0] + pointB[0] + pointC[0]) / 3.0
    b = (pointA[1] + pointB[1] + pointC[1]) / 3.0
    return [round(a, 4), round(b, 4)]
