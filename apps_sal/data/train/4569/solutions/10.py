def next_item(xs, item):
    items = iter(xs)
    for thing in items:
        try:
            if thing == item:
                return next(items)
        except StopIteration:
            return None
    return None
