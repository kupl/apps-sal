from math import acos, sqrt, pi, atan2


def eucelid(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def cpd(x, y, z):
    cpd = (y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0])
    if cpd < 0:
        return -1
    if cpd > 0:
        return 1
    return 0


def cc(s, z):
    (x_s, y_s) = (s[0] - z[0], s[1] - z[1])
    return atan2(y_s, x_s)


def hull_method(pointlist):
    (d, stack) = (min(pointlist, key=lambda x: (x[1], x[0])), [])
    pointlist.sort(key=lambda x: (cc(x, d), eucelid(x, d)))
    stack += pointlist[:2]
    for i in range(2, len(pointlist)):
        (nx, pp) = (pointlist[i], stack.pop())
        while len(stack) and stack[-1] and (cpd(stack[-1], pp, nx) <= 0):
            pp = stack.pop()
        stack += [pp, nx]
    return stack
