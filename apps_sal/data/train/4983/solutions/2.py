def merge(*dicts):
    r={}
    for d in dicts:
        for k in d:
            r[k]=r.get(k,[])+[d[k]]
    return r
