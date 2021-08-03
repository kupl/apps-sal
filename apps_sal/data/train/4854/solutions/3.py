import math


def count_circles(loc, point):
    c = 0
    px, py = point
    for i in range(0, len(loc)):
        circle = circum_curvat(loc[i][0], loc[i][1], loc[i][2])
        if circle != False:
            x, y, r = circle
            d = ((x - px)**2 + (y - py)**2)**.5
            if d <= r + 1e-10:
                c += 1
    return c


def circum_curvat(pointA, pointB, pointC):
    xA, yA = pointA
    xB, yB = pointB
    xC, yC = pointC
    if pointA == pointB or pointA == pointC or pointC == pointB:
        return False
    x = (xA**2 + yA**2) * (yB - yC) + (xB**2 + yB**2) * (yC - yA) + (xC**2 + yC**2) * (yA - yB)
    y = (xA**2 + yA**2) * (xC - xB) + (xB**2 + yB**2) * (xA - xC) + (xC**2 + yC**2) * (xB - xA)
    AB = ((xB - xA)**2 + (yB - yA)**2)**.5
    BC = ((xC - xB)**2 + (yC - yB)**2)**.5
    AC = ((xC - xA)**2 + (yC - yA)**2)**.5
    D = 2.0 * (xA * (yB - yC) + xB * (yC - yA) + xC * (yA - yB))
    if D == 0:
        return False
    Ux = x / D
    Uy = y / D
    if D < 0:
        D = -D
    diam = AB * BC * AC / D
    return [Ux, Uy, diam]
