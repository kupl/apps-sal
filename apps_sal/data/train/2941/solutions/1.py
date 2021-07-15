def add(*args):
    return round(sum(x / i for i, x in enumerate(args, 1)))

