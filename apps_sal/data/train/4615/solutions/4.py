def smallest_dist(x, y, xs, ys):
    min = None
    for i in range(len(xs)):
        v = abs(xs[i] - x) + abs(ys[i] - y)
        min = (min, v)[min == None or min > v]
    return min


def logistic_map(w, h, xs, ys):
    return [[smallest_dist(x, y, xs, ys) for x in range(w)] for y in range(h)]
