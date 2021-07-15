def next_item(xs, item):
    it = iter(xs)
    return None if item not in it else next(it, None)
