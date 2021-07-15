def next_item(xs, item):
    found = False
    for i in xs:
        if found:
            return i
        if i == item:
            found = True
    else:
        return None

