def next_item(xs, item):
    itemFound = False
    for i in xs:
        if itemFound:
            return i
        if i == item:
            itemFound = True
