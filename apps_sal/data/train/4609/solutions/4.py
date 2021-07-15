def egged(year, span):
    NBASE, NCB = 300, 3
    if year < 1:
        return "No chickens yet!"
    nc = []
    ttl = []
    n = 0
    nc.append(NBASE)
    ttl.append(span)
    for i in range(year):
        for k in range(len(nc) - 1, -1, -1):
            n += nc[k] * NCB
            ttl[k] -= 1
            if ttl[k] < 1:
                nc.pop(k)
                ttl.pop(k)
            else:
                nc[k] = nc[k] * 4 // 5
    return n
