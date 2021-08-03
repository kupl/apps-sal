def next_item(xs, item):
    found = False
    for i in xs:
        if found:
            return i
            break
        elif i == item:
            found = True
