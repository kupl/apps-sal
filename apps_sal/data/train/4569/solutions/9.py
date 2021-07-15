def next_item(xs, item, trap = None):
    for i in xs:
        if trap:
            return i
        if i == item:
            trap = True
