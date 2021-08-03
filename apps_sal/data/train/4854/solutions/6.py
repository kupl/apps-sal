import math


def circum_curvat(pointA, pointB, pointC):
    # if len({pointA, pointB, pointC})<3:
    #    return (0,0,0)
    D = 2 * (pointA[0] * (pointB[1] - pointC[1]) + pointB[0] * (pointC[1] - pointA[1]) + pointC[0] * (pointA[1] - pointB[1]))
    if abs(D) < 1e-10:
        return (0, 0, 0)
    x = ((pointA[0]**2 + pointA[1]**2) * (pointB[1] - pointC[1]) +
         (pointB[0]**2 + pointB[1]**2) * (pointC[1] - pointA[1]) +
         (pointC[0]**2 + pointC[1]**2) * (pointA[1] - pointB[1])
         ) / D
    y = ((pointA[0]**2 + pointA[1]**2) * (pointC[0] - pointB[0]) +
         (pointB[0]**2 + pointB[1]**2) * (pointA[0] - pointC[0]) +
         (pointC[0]**2 + pointC[1]**2) * (pointB[0] - pointA[0])
         ) / D

    ab = math.hypot(pointB[0] - pointA[0], pointB[1] - pointA[1])
    bc = math.hypot(pointB[0] - pointC[0], pointB[1] - pointC[1])
    ac = math.hypot(pointC[0] - pointA[0], pointC[1] - pointA[1])
    radius = ab * bc * ac / abs(D)
    return (x, y, radius)


def count_circles(list_of_circles, point):
    result = 0
    for circles in list_of_circles:
        x, y, r = circum_curvat(*circles)
        if r - math.hypot(point[0] - x, point[1] - y) > -1e-10:
            result += 1
    return result
