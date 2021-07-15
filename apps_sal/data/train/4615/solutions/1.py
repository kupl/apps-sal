def logistic_map(w, h, xs, ys):
    md = lambda i, j: min((abs(x - i) + abs(y - j) for x, y in zip(xs, ys)), default=None)
    return [[md(i, j) for i in range(w)] for j in range(h)]


