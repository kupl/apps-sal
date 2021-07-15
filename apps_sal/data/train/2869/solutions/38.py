def distinct(seq):
    uniq_seq =[]
    for el in seq:
        if el not in uniq_seq:
            uniq_seq.append(el)
    return uniq_seq

