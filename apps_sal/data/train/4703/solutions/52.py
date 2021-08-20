def bar_triang(pointA, pointB, pointC):
    (x, y, lst) = (0, 0, [pointA, pointB, pointC])
    for i in range(3):
        x += lst[i][0]
        y += lst[i][1]
    return [round(x / 3, 4), round(y / 3, 4)]
