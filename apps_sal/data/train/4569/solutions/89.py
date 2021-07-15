def next_item(xs, item):
    it = iter(xs)
    for value in it:
        if value == item:
            return next(it, None)
    return None
