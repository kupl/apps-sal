def next_item(xs, item):
    xs = iter(xs)
    try:
        while (next(xs) != item):
            pass
        return next(xs)
    except:
        return None
