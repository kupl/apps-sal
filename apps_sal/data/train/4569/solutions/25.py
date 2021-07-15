def next_item(xs, item):
    it = iter(xs)
    next((x for x in it if x == item), None)
    return next(it, None)

