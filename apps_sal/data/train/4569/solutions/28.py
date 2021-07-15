def next_item(xs, item):
    object = iter(xs)
    for el in object:
        if el == item:
            break
    return next(object, None)
