def make_sequences(n):
    seq = [0]
    for _ in range(1000):
        seq.append(1 + sum((seq[i + 1] for i in range(len(seq) // 2))))
    return seq[n]
