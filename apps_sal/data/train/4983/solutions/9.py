def merge(*dicts):
    r = {}
    for d in dicts:
        for k, v in d.items():
            if k in r: r[k].append(v)
            else: r[k] = [v]
    return r
