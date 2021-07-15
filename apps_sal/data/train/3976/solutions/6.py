def last(*args):
    try:
        count = len(args[-1])
        return args[-1][-1]
    except TypeError:
        return args[-1]
