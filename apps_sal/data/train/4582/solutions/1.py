from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


def group(arr):
    return [[k] * v for (k, v) in OrderedCounter(arr).items()]
