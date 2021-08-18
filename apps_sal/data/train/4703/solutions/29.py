def bar_triang(pointA, pointB, pointC):
    xO = round(sum(x[0] for x in [pointA, pointB, pointC]) / 3, 4)
    yO = round(sum(y[1] for y in [pointA, pointB, pointC]) / 3, 4)
    return [xO, yO]
