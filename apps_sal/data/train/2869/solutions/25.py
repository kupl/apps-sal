def distinct(seq):

    seq2 = []
    for i in seq:
        if i not in seq2:
            seq2.append(i)
    return seq2
