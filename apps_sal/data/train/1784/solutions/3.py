def curry_partial(f, *initial_args):
    if not callable(f):
        return f
    exp_n_args = f.__code__.co_argcount
    given_n_args = len(initial_args)
    if exp_n_args - given_n_args > 0:
        return lambda *args: curry_partial(f, *initial_args + args)
    if exp_n_args == 0:
        return f(*initial_args)
    else:
        return f(*initial_args[:exp_n_args])
