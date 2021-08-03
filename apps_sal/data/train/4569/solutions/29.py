def next_item(xs, item):
    stop = False
    for el in xs:
        if stop:
            return el
        elif el == item:
            stop = True
