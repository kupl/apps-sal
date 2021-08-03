from functools import partial


def collinear(p1, p2, p3):
    return (p3[1] - p2[1]) * (p2[0] - p1[0]) == (p2[1] - p1[1]) * (p3[0] - p2[0])


def on_line(points):
    points = list(set(points))
    return all(map(partial(collinear, *points[:2]), points[2:]))
