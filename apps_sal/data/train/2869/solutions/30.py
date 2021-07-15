def distinct(seq):
    return sorted(set(seq), key=lambda d: seq.index(d))
