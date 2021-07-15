def next_item(xs, item):
    cursor = iter(xs)
    while True:
        try:
            element = next(cursor)
            if element == item:
                return next(cursor)
        except StopIteration:
            return
