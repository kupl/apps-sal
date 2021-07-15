def array_mash(xs, ys):
    return [z for p in zip(xs, ys) for z in p]
