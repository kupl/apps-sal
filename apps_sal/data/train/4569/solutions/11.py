def next_item(xs, item):
    (ans, trap) = (None, False)
    for i in xs:
        if trap:
            return i
        if i == item:
            trap = True
    return None
