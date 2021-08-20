def bar_triang(pointA, pointB, pointC):
    return [round((a + b + c) / 3, 4) for (a, b, c) in zip(pointA, pointB, pointC)]
