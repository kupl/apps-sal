def merge_arrays(f, s):
    t = f + s
    res = sorted(t)
    res = set(res)
    return list(sorted(res))
    

