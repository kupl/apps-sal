def add(*args):
    return int(round(sum((float(a) / i for (i, a) in enumerate(args, 1)))))
