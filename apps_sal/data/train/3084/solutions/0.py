def combine(*bs):
    c = {}
    for b in bs:
        for k, v in list(b.items()):
            c[k] = v + c.get(k, 0)
    return c
