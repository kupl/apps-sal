def next_item(xs, item):
    found = False
    for i in xs:
        if found:
            return i
        else:
            found = i == item
