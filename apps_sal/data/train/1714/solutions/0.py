def hull_method(points):
    sorted_points = sorted(points)
    return half_hull(sorted_points) + half_hull(reversed(sorted_points))

def half_hull(sorted_points):
    hull = []
    for p in sorted_points:
        while len(hull) > 1 and not is_ccw_turn(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull

def is_ccw_turn(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]) > 0

