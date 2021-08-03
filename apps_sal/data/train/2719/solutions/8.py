def add(*args):
    return sum(n * (i + 1) for i, n in enumerate(args)) if args else 0
