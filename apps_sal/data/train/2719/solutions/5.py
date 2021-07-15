def add(*args):
    return sum((i+1) * args[i] for i in range(len(args)))
