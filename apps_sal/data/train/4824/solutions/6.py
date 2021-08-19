# Computational complexity of 1.5n
def get_min_max(seq):
    seq = iter(seq)
    seq_min = seq_max = next(seq)

    while True:
        try:
            a = next(seq)
        except StopIteration:
            break

        b = next(seq, seq_min)
        if a > b:
            seq_min = min(b, seq_min)
            seq_max = max(a, seq_max)
        else:
            seq_min = min(a, seq_min)
            seq_max = max(b, seq_max)

    return seq_min, seq_max
