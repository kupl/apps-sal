def combine(*args):
    ret = {}
    for arg in args:
        for (k, v) in arg.items():
            ret.setdefault(k, 0)
            ret[k] = ret[k] + v
    return ret
