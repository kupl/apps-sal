def compose(f, g):
    def z(*arg, **kw):
        return f(g(*arg, **kw))
    return z
