from itertools import groupby


def distinct(seq):
    seq_new = []
    for i in seq:
        if i not in seq_new:
            seq_new.append(i)
    return seq_new
