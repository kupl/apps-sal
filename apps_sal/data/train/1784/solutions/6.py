def curry_partial(f, *initial_args):
    def f1(*args):
        def f2(*args2):

            if not callable(f):
                return f
            elif f.__code__.co_argcount == 0:
                return f(*(args + args2))
            elif f.__code__.co_argcount > len(args + args2):
                return f1(*(args + args2))
            else:
                return f(*(args + args2)[0:f.__code__.co_argcount])

        return f2
    return f1(*initial_args)()
