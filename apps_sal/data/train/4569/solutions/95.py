def next_item(xs, item):
    it = iter(xs)
    for e in it:
        if e == item:
            break
    else:
        return
    for e in it:
        return e
