def regressionLine(xs, ys):
    sx, sy, sxy = sum(xs), sum(ys), sum(x*y for x, y in zip(xs, ys))
    n, sx2, s2x = len(xs), sum(x*x for x in xs), (sx*sx)
    return tuple(round(d / (n*sx2 - s2x), 4) for d in (sx2*sy - sx*sxy, n*sxy - sx*sy))
