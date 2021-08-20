def shuffle_it(a, *args):
    for (x, y) in args:
        (a[x], a[y]) = (a[y], a[x])
    return a
