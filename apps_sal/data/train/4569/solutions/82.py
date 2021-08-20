def next_item(xs, item):
    for (i, x) in enumerate(xs):
        try:
            if x == item and i != len(xs) - 1:
                return xs[i + 1]
        except:
            return next(xs)
