def next_item(xs, item):
    iterable = iter(xs)
    for x in iterable:
        if x == item:
            break
    return next(iterable, None)
