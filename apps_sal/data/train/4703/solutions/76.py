def bar_triang(pointA, pointB, pointC):
    return [round(x / 3, 4) for x in [sum(i) for i in zip(pointA, pointB, pointC)]]
