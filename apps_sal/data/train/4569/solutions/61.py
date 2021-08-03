def next_item(xs, item):
    # TODO: Implement me
    a = iter(xs)
    while(True):
        try:
            if next(a) == item:
                return next(a)
        except:
            return None
