def count_targets(n, seq):
    return sum((a == b for (a, b) in zip(seq, seq[n:])))
