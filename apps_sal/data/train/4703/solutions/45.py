def bar_triang(pointA, pointB, pointC):
    return [round(sum((x / 3 for (x, _) in [pointA, pointB, pointC])), 4), round(sum((y / 3 for (_, y) in [pointA, pointB, pointC])), 4)]
