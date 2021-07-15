from collections import Iterable

def last(*args):
    return args[-1][-1] if isinstance(args[-1], Iterable) else args[-1]
