def count_targets(n, sequence):
    return sum(1 for a, b in zip(sequence, sequence[n:]) if a == b)
