def substring(stg):
    i, mi, s, ms, l = 0, 0, 3, 2, len(stg)
    while i + s <= l:
        if len(set(stg[i:i+s])) > 2:
            i += 1
        else:
            mi, ms = i, s
            s += 1
    return stg[mi:mi+ms]


