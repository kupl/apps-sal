def distinct(seq):
    seq1 = list()
    for i in seq:
        if i not in seq1:
            seq1.append(i)
    return seq1
