def uniq(seq):
    if len(seq) == 0:
        return []
    rez = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i] != rez[-1]:
            rez.append(seq[i])
    return rez
