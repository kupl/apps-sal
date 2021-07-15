from itertools import groupby

def group_in_10s(*args):
    if not args: return []
    res = [None] * (1 + max(args) // 10)
    for a, b in groupby(args, key = lambda x: x // 10):
        if res[a] == None:
            res[a] = sorted(list(b))
        else:
            res[a] = sorted(res[a] + list(b))
    return res

