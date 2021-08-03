def next_item(a, item):
    found = 0
    for e in a:
        if found:
            return e
        if e == item:
            found = 1
