from numpy import cross, subtract


def convex_hull_area(points):
    if len(points) < 3:
        return 0
    area = 0
    for direction in 1, -1:
        hull = []
        for point in sorted(points)[::direction]:
            while len(hull) > 1 and cross(*hull[-2:]) < cross(point, -subtract(*hull[-2:])):
                hull.pop()
            hull.append(point)
        area += sum(cross(hull[i - 1], point) for i, point in enumerate(hull)) / 2
    return round(area, 2)
