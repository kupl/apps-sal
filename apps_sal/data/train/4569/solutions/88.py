def next_item(xs, item):
    if type(xs) == list:
        if xs.count(item) == 0:
            return None
        q = xs.index(item)
        if (q + 1) >= len(xs):
           return None
        return xs[q + 1]
    else:
        qq = 0
        for i in xs:
            if i == item and qq == 0:
                qq = 1
                continue
            if qq == 1:
                return i
        return None
