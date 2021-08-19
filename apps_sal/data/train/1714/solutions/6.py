from math import atan2, pi
tau = 2 * pi


def hull_method(pointlist):
    pointlist = sorted(set(((x, y) for [x, y] in pointlist)))
    s = min(pointlist, key=lambda p: p[1])
    p = s
    d = 0
    l = []
    while p != s or len(l) < 1:
        tp = min([(x - p[0], y - p[1]) for (x, y) in pointlist if x != p[0] or y != p[1]], key=lambda p: ((atan2(p[1], p[0]) - d + tau) % tau, -p[0] ** 2 - p[1] ** 2))
        p = (tp[0] + p[0], tp[1] + p[1])
        l.append(p)
        d = (atan2(tp[1], tp[0]) + tau) % tau
    return [[x, y] for (x, y) in l]
