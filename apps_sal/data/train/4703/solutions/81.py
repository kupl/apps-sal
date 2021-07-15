def bar_triang(pointA, pointB, pointC):
    return list(map(lambda x: round(sum(x) / 3, 4), zip(pointA, pointB, pointC)))
