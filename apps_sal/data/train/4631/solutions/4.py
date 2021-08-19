def createDict(keys, vals):
    res = {}
    for (i, key) in enumerate(keys):
        res[key] = vals[i] if i < len(vals) else None
    return res
