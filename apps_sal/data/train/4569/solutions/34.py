def next_item(xs, item):
    after = False
    for i in xs:
        if after:
            return i
        if i == item:
            after = True
