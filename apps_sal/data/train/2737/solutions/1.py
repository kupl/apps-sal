def near_flatten(xs):

    def f(xs):
        if all((not isinstance(x, list) for x in xs)):
            yield xs
            return
        for x in xs:
            yield from f(x)
    return sorted(f(xs))
