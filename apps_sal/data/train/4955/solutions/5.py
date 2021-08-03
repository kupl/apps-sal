from functools import reduce


def ride(group, comet):
    return "GO" if score(group) == score(comet) else "STAY"


def score(word):
    return reduce(int.__mul__, (ord(c) - 64 for c in word)) % 47
