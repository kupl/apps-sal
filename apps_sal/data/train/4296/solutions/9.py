def largest(n, xs):
    """Find the n highest elements in a list"""
    return (sorted(xs, reverse=True)[0:n])[::-1]
