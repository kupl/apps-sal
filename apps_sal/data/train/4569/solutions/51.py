def next_item(xs, item):
    found = False
    for i in xs:
        if i == item:
            found = True
        elif found == True:
            return i
