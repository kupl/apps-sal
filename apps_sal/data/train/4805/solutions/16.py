from operator import contains as check


def check(seq, elem):
    return elem in set(seq)


def check(seq, elem):
    return elem in seq
