def next_item(xs, item):
    i = None
    for (count, element) in enumerate(xs):
        if element == item:
            i = count + 1
            continue
        if i is not None:
            return element
    return None
