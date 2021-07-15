def count_targets(n, sequence):
    return sum([1 for i in range(n, len(sequence)) if sequence[i] == sequence[i-n]])
