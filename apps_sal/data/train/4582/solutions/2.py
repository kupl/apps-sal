from collections import OrderedDict

def group(arr):
    d = OrderedDict()
    for x in arr:
        d.setdefault(x, []).append(x)
    return list(d.values())
