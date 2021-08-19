def compose(f, g):
    # Compose the two functions here!
    def z(*arg, **kw):
        return f(g(*arg, **kw))
    return z
