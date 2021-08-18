def bar_triang(pointA, pointB, pointC):
    x0 = float(f'{(pointA[0] + pointB[0] + pointC[0])/3 : .4f}')
    y0 = float(f'{(pointA[1] + pointB[1] + pointC[1])/3 : .4f}')
    return [x0, y0]
