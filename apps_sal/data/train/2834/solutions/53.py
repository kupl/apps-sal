def symmetric_point(p, q):
    deltax = q[0]-p[0]
    deltay = q[1]-p[1]
    p1 = []
    p1.append(q[0]+deltax)
    p1.append(q[1]+deltay)
    return p1
