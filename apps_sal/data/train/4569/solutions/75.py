def next_item(xs, item):
    itr = iter(xs)
    for elem in itr:
        if elem == item:
            break
    return next(itr, None)

