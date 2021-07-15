def bar_triang(pointA, pointB, pointC):
    return [round(i,4) for i in list(map(lambda x, y, z: (x + y + z) / 3, pointA, pointB, pointC))]
