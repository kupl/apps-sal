from collections import OrderedDict


def unite_unique(*xss):
    return list(OrderedDict.fromkeys((x for xs in xss for x in xs)))
