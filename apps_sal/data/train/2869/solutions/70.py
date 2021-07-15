def distinct(seq):
    return [i[1] for i in enumerate(seq) if i[1] not in seq[:i[0]]]
