from collections import OrderedDict
def unite_unique(*arrs):
    arrs = [x for arr in arrs for x in arr]
    return [x for i, x in enumerate(arrs) if i == arrs.index(x)]

