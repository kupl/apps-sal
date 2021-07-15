def add(*args):
    return sum((i + 1) * n for i, n in enumerate(args))
