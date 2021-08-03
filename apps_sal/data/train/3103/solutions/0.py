from collections import OrderedDict


def unique(integers):
    return list(OrderedDict.fromkeys(integers))
