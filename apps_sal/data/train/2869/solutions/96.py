def distinct(seq):
    import collections
    return [i for i in dict(collections.Counter(seq))]
