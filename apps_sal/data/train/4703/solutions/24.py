def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    return list(map(lambda x: round(sum(x) / 3, 4), zip(pointA, pointB, pointC)))
