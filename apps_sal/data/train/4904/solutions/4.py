def unpack(L):
    res = []
    for el in L:
        if isinstance(el, (list, tuple, set)):
            res.extend(unpack(el))
        elif isinstance(el, dict):
            res.extend(unpack(el.items()))
        else:
            res.append(el)
    return res
