def dist(pointA, pointB):
    return ((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)**.5


def contains(circle, point):
    return circle and 0 <= circle['r'] - dist(point, circle['c']) <= circle['r'] or abs(circle['r'] - dist(point, circle['c'])) / circle['r'] < 1e-10


def circum_curvat(points):
    if len(set(map(tuple, points))) != 3:
        return None
    xa, ya, xb, yb, xc, yc = points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1]
    D = 2. * (xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb))
    if not D:
        return None
    Ux = ((xa**2 + ya**2) * (yb - yc) + (xb**2 + yb**2) * (yc - ya) + (xc**2 + yc**2) * (ya - yb)) / D
    Uy = ((xa**2 + ya**2) * (xc - xb) + (xb**2 + yb**2) * (xa - xc) + (xc**2 + yc**2) * (xb - xa)) / D
    rad = dist(points[0], points[1]) * dist(points[1], points[2]) * dist(points[0], points[2]) / abs(D)
    return {'c': (Ux, Uy), 'r': rad}


def count_circles(list_of_circles, point):
    return len(filter(None, (contains(circum_curvat(p), point) for p in list_of_circles)))
