def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    return [round(x / 3, 4) for x in [sum(i) for i in zip(pointA, pointB, pointC)]]
