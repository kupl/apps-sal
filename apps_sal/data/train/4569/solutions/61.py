def next_item(xs, item):
    a = iter(xs)
    while True:
        try:
            if next(a) == item:
                return next(a)
        except:
            return None
