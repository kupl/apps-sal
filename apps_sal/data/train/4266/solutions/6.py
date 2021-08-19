def min_dot(a, b):

    def dot(xs, ys):
        return sum((x * y for (x, y) in zip(xs, ys)))
    return dot(sorted(a), sorted(b, reverse=True))
