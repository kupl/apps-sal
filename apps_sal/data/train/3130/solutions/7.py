def has_subpattern(stg):
    l = len(stg)
    for k in range(2, int(l ** 0.5) + 1):
        if l % k == 0:
            if any((len({stg[i:i + s] for i in range(0, l, s)}) == 1 for s in (l // k, k))):
                return True
    return False
