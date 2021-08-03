def curry_partial(fn, *x):
    if not callable(fn):
        return fn
    size = fn.__code__.co_argcount or None
    return fn(*x[:size]) if size <= len(x) else lambda *y: curry_partial(fn, *(x + y))
