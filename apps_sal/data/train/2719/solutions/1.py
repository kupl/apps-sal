def add(*args):
    return sum((n * i for (i, n) in enumerate(args, 1)))
