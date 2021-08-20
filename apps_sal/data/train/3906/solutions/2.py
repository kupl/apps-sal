def total(xs):
    return xs[0] if len(xs) == 1 else total([xs[i] + x for (i, x) in enumerate(xs[1:])])
