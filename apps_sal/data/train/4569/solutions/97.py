def next_item(xs, item):
    if type(xs) is str:
        xs = [x for x in xs]
    if type(xs) is list:
        xs = (x for x in xs)
    for x in xs:
        if x == item:
            try:
                return next(xs)
            except StopIteration:
                return None
    return None
