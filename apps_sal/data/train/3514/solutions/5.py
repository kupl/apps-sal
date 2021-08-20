def validate_sequence(sequence):
    return len(set([n - p for (p, n) in zip(sequence, sequence[1:])])) == 1
