def uniq_c(seq):
    new_seq = list()
    count = 0
    for i in range(len(seq)):
        if i == 0:
            new_seq.append(seq[i])
            count += 1
            continue
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            new_seq[-1] = (seq[i - 1], count)
            count = 1
            new_seq.append(seq[i])

    if len(seq) != 0:
        new_seq[-1] = (seq[-1], count)

    return new_seq
