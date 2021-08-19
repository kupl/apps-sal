def distinct(seq):
    return [x for (i, x) in enumerate(seq) if i == seq.index(x)]
