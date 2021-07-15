def next_item(xs, item):
    lst = iter(xs)
    for x in lst:
        if x == item:
            break
    return next(lst, None)
