from collections import OrderedDict


def unite_unique(*lists):
    return list(OrderedDict.fromkeys(sum(lists, [])))
