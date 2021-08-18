def curry_partial(f, *args):
    if not callable(f):
        return f
    try:
        return f(*args)
    except:
        pass
    try:
        return f()
    except:
        pass
    if args:
        return curry_partial(lambda *a: f(args[0], *a), *args[1:])
    else:
        return lambda *a: curry_partial(f, *a)
