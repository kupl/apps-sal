def add(*args):
    return sum((pos * value for (pos, value) in enumerate(args, 1)))
