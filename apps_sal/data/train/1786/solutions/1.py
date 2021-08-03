def cross(p1, p2, p):
    return (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])


def dist_to(p1):
    def f(p):
        return (p1[0] - p[0]) * (p1[0] - p[0]) + (p1[1] - p[1]) * (p1[1] - p[1])
    return f


def xy_yx(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def convex_hull_area(pts):
    if len(pts) == 0:
        return 0
    pts = set(pts)
    new = min(pts)
    head = new
    area = 0
    while 1:
        tail = new
        d_fn = dist_to(tail)
        new = next(iter(pts))
        for test in pts:
            if test != new and test != tail:
                c = cross(tail, new, test)
                if tail == new or c > 0:
                    new = test
                elif c == 0:
                    new = max(new, test, key=d_fn)
        area += xy_yx(tail, new)
        if new is head:
            return round(abs(area) / 2.0, 2)
