from collections import Counter


def only_one(*booleans):
    return Counter(booleans)[True] == 1
