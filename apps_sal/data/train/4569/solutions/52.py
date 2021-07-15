def next_item(xs, item):
    i = iter(xs)
    try:
        while next(i) != item:
            pass
        return next(i)
    except StopIteration:
        return None
