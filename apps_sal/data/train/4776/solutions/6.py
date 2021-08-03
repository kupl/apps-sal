def length_sup_u_k(n, k):
    return len([x for x in fibSeq(n) if x >= k])


def comp(n):
    seq = fibSeq(n)
    return len([x for x in range(1, len(seq)) if seq[x] < seq[x - 1]])


def fibSeq(n):
    sequence = [1, 1]

    for i in range(2, n):
        sequence.append(sequence[i - sequence[i - 1]] + sequence[i - sequence[i - 2]])
    return sequence
