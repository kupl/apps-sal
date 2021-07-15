def next_item(xs, item):
    xs = xs.__iter__()
    while True:
        try:
            if next(xs) == item: return next(xs)
        except: break
