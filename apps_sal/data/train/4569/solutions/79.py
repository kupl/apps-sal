def next_item(xs, item):
    print((xs, item))
    print(type(xs))
    if type(xs) == str:
        print(xs[-2:-1])
        return xs[xs.index(item) + 1:xs.index(item) + 2] if xs[-1:] != item and item in xs else None
    if type(xs) == list:
        if item in xs and (not item == xs[-1]):
            return xs[xs.index(item) + 1]
        else:
            return None
    else:
        p = 0
        for k in xs:
            if p == 1:
                return k
            if k == item:
                p = 1
        return None
