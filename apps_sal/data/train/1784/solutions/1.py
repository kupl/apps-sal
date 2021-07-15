def curry_partial(f, *args):
    if not callable(f): return f # ignore extra args
    try: return f(*args) # handle nested currying
    except: pass
    try: return f() # ignore extra args if we are done
    except: pass
    if args: return curry_partial(lambda *a: f(args[0], *a), *args[1:]) # curry
    else: return lambda *a: curry_partial(f, *a) # leave to caller

