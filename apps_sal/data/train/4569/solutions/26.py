def next_item(xs, item):
    xl = (i for i in xs)
    try:
        while next(xl) != item:
            continue
        return next(xl)
    except StopIteration:
        pass
