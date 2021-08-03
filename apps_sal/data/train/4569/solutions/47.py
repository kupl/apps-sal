def next_item(xs, item):
    iterator = iter(xs)
    for i in iterator:
        if i == item:
            return next(iterator, None)

    return None
