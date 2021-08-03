def next_item(xs, item):
    it = iter(xs)
    try:
        while next(it) != item:
            pass
        return next(it)
    except:
        return None
