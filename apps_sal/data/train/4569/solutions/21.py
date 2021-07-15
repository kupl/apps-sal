def next_item(xs, item):
    f = int(1)
    for x in xs:
        if f == 0:
            f = 1
            return x
        if x == item:
            f = 0
    # TODO: Implement me

