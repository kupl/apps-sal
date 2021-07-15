def next_item(xs, item):
    found = False
    for e in xs:
        if found:
            return e
        if e==item:
            found = True
    return None

