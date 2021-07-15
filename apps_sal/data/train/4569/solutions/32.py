def next_item(xs, item):
    end = False
    for i in xs:
        if end:
            return i
        if i == item:
            end = True
