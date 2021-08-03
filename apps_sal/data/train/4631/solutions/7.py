import itertools


def createDict(keys, values):
    return dict(zip(keys, itertools.chain(values, itertools.repeat(None))))
