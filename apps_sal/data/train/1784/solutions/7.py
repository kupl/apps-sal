from inspect import getfullargspec


def curry_partial(f, *initial_args, arg_spec=None):
    if not arg_spec:
        if not callable(f):
            return f
        arg_spec = getfullargspec(f)
    param_l = len(arg_spec.args)
    if param_l < len(initial_args) + 1:
        if arg_spec.varargs:
            return f(*initial_args)
        else:
            return f(*initial_args[:param_l])
    else:
        def fun(*args):
            return curry_partial(f, *(initial_args + args), arg_spec=arg_spec)
        return fun
