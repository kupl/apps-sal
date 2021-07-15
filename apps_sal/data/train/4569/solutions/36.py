def next_item(xs, item):
    f = False
    for i in xs:
        if f:
            return i
        if i == item:
            f = True
