def distinct(seq):
    new_seq = []
    [new_seq.append(seq[i]) for i in range(len(seq)) if seq[i] not in new_seq]
    return new_seq
