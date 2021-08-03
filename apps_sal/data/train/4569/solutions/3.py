def next_item(xs, item):
    ret = False
    for x in xs:
        if ret:
            return x
        if item == x:
            ret = True
