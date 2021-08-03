def next_item(xs, item):
    mark = False
    for i in xs:
        if mark:
            return i
        if i == item:
            mark = True
