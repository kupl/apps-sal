def next_item(xs, item):
    r = False
    for i in xs:
        if r:
            return i
        elif i == item:
            r = True
    return None
