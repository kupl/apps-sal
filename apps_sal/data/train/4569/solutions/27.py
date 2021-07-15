def next_item(xs, item):
    it = iter(xs)
    next(iter(el for el in it if el == item), None)
    return next(it, None)
