def next_item(xs, item):
    if type(xs) is str or type(xs) is list:
        for i in range(len(xs)):
            if xs[i] == item and xs.index(xs[i]) < xs.index(xs[-1]):
                return xs[i + 1]
        return None
    else:
        j = 0
        for j in xs:
            if j == item:
                return next(xs)
