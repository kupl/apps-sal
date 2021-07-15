def next_item(xs, item):
    f = 0
    for x in xs:
        if f: return x
        if x == item: f = 1
