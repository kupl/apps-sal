def odd_one_out(s):
    d = {}
    for i in s:
        if i in d:
            del d[i]
        else:
            d[i] = None
    return list(d.keys())
