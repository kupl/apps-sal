def next_item(xs, item):
    found = None
    for x in xs:
        if found:
            return x
        if x == item:
            found = True
    return None
