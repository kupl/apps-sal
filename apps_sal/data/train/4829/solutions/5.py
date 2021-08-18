def compose(f, g):
    def newfunc(*args):
        return f(g(*args))
    return newfunc
