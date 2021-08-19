import inspect


def curry_partial(f, *args):
    if not callable(f):
        return f
    req = list(inspect.signature(f).parameters)
    return f(*args) if req and req[0] == '_e' else f(*args[:len(req)]) if len(req) <= len(args) else lambda *_e: curry_partial(f, *args + _e)
