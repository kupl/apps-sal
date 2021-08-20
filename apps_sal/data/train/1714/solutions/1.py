def get_direction(a, b, c, d, e, f):
    (x1, y1) = (c - a, d - b)
    (x2, y2) = (e - a, f - b)
    return x1 * y2 - x2 * y1


def get_distance(a, b, c, d):
    return (abs(c - a) ** 2 + abs(d - b) ** 2) ** 0.5


def hull_method(points):
    index = points.index(min(points))
    (length, border, track) = (len(points), [], index)
    while True:
        nxt = (track + 1) % length
        for i in range(length):
            if i != track:
                d = get_direction(*points[track], *points[i], *points[nxt])
                if d > 0 or (d == 0 and get_distance(*points[track], *points[i]) > get_distance(*points[track], *points[nxt])):
                    nxt = i
        track = nxt
        border.append(points[track])
        if track == index:
            break
    return sorted(border)
