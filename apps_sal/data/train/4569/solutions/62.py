def next_item(xs, item):
    if hasattr(xs, '__iter__') and hasattr(xs, '__next__'):
        for x in xs:
            if x == item:
                return next(xs)
    if xs == [] or item not in xs:
        return None
    if xs.index(item) == len(xs) - 1:
        return None
    return xs[xs.index(item) + 1]
