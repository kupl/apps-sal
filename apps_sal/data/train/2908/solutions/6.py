def flatten(d):
    r = {}
    for (x, y) in d.items():
        if isinstance(y, dict):
            r.update({f'{x}/{X}': Y for (X, Y) in flatten(y).items()} if y else {x: ''})
        else:
            r[x] = y
    return r
