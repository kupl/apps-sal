def add(*args):
    return round(sum(1.0 * n / i for i, n in enumerate(args, 1)))
