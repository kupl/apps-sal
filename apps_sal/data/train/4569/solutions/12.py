def next_item(xs, item):
    xs = iter(xs)
    for x in xs:
        if x == item:
            break
    return next(xs, None)
