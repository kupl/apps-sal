def distinct(seq):
    new_seq = []
    for c in seq:
        if c not in new_seq:
            new_seq.append(c)
    return new_seq
