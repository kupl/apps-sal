
def combine(*args):
    keys = set([y for x in args for y in list(x.keys())])
    return {k: sum([a.get(k, 0) for a in args]) for k in keys}
