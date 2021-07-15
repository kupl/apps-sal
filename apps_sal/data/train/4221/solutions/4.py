def count_targets(n, sequence):
    return sum(y == x for x, y in zip(sequence, sequence[n:]))
