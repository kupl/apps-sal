def distinct(seq):
    return [seq[i] for i in range(len(seq)) if seq[i] not in seq[:i] + seq[i + 1:] or i == seq.index(seq[i])]
