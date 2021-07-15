def next_item(xs, item):
    found = False
    for x in xs:
        if x == item:
            found = True
        elif found:
            return x
    return
