def compose(f, g):

    def composing(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composing
