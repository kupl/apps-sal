def logistic_map(width, height, xs, ys):

    supply_stops = zip(*[xs, ys])
    points = [[None for x in range(width)] for x in range(height)]

    for s in supply_stops:
        for i in range(width):
            for j in range(height):
                d_cur = abs(s[0] - i) + abs(s[1] - j)
                d_pnt = points[j][i]

                if (d_pnt == None) or (d_cur < d_pnt):
                    points[j][i] = d_cur
    return points
