def spread(func, args):
    if len(args) == 2:
        return func(args[0], args[1])
    elif len(args) == 3:
        return func(args[0], args[1], args[2])
