from collections import defaultdict

def merge(*dicts):
    d = defaultdict(list)
    for dd in dicts:
        for k,v in dd.items():
            d[k].append(v)
    return d
