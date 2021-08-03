def next_item(xs, item):
    if item not in xs:
        return None
    if type(xs) in [str, list]:
        return None if item not in xs[:-1] else xs[xs.index(item) + 1]
    return next(xs)
