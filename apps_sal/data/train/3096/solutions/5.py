def josephus(items, k):
    out = []
    i = 0
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        out.append(items[i])
        del items[i]
    return out
