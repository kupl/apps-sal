def next_item(xs, item):
    it = iter(xs)
    if item in it:
        try:
            return next(it)
        except:
            pass
