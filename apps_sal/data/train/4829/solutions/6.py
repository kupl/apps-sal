def compose(f, g):
    return lambda *a, **kw: f(g(*a, **kw))
