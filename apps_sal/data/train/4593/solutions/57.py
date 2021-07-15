def merge_arrays(x, y):
    res = []
    while True:
        if len(x) == 0:
            res.extend(y)
            break
        if len(y) == 0:
            res.extend(x)
            break
        first, second = x[0], y[0]
        if first < second:
            res.append(first)
            x.pop(0)
        else:
            res.append(second)
            y.pop(0)
    return sorted(set(res))
