def last(*args):
    import collections
    if len(args) == 1:
        if isinstance(args[0], collections.Iterable):
            return args[0][-1]
        else:
            return args[0]
    else:
        return args[-1]
