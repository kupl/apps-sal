def next_item(xs, item):
    ret = False
    for j in xs:
        if ret:
            return j
        if j == item:
            ret = True
