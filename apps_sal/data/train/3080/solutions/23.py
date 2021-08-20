from collections import OrderedDict


def who_is_paying(n):
    return list(OrderedDict.fromkeys([n, n[0:2]]))
