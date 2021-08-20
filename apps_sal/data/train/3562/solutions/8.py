def count_inversion(sequence):
    return sum([sum([1 if sequence[x] > sequence[x + y] else 0 for y in range(1, len(sequence) - x)]) for x in range(len(sequence))])
