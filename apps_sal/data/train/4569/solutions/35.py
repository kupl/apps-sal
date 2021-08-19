def next_item(xs, item):
    iter_obj = iter(xs)
    while True:
        try:
            element = next(iter_obj)
            if element == item:
                element = next(iter_obj)
                return element
        except StopIteration:
            break
            return None
