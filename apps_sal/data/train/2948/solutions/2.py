def split_by_value(k, elements):
    res = [[], []]
    for x in elements:
        res[k <= x].append(x)
    return res[0] + res[1]
