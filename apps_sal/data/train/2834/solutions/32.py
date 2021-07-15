def symmetric_point(p, q):
    pointslist = []
    difference = q[0] - p[0]
    newpoint = q[0] + difference
    difference2 = q[1] - p[1]
    newpoint2 = q[1] + difference2
    pointslist.append(newpoint)
    pointslist.append(newpoint2)
    return pointslist
