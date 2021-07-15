def near_flatten(a):
    r = []
    for x in a:
        if isinstance(x[0], int): r.append(x)
        else: r.extend(near_flatten(x))
    return sorted(r)
