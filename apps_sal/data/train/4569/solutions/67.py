def next_item(xs, item):
    n = False
    for x in xs:
        if n: return x
        if x == item: n = True
