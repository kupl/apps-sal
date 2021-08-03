def bar_triang(pointA, pointB, pointC):
    return [round(sum(i) / 3, 4) for i in zip(pointA, pointB, pointC)]
