def next_item(xs, item):
    it = iter(xs)
    for i in it:
        if i == item:
            return next(it, None)
    return None
