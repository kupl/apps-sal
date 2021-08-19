def add(*args):
    return sum((i * x for (i, x) in enumerate(args, 1)))
