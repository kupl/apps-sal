def next_item(xs, item):
    iterator = iter(xs)
    for x in iterator:
        if x == item:
            return next(iterator, None)
    return None
