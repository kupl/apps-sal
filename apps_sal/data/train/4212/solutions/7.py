from collections import OrderedDict
def unite_unique(*args):
    return list(OrderedDict.fromkeys(sum([a for a in args], [])))
