def unique_in_order(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r
