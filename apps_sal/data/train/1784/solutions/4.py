def curry_partial(f, *args):
    if not callable(f):
        return f
    if len(args) < f.__code__.co_argcount:
        return lambda *a: curry_partial(f, *args + a)
    return f(*args[:f.__code__.co_argcount or None])
