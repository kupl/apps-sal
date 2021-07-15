def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    return sum(n > m for i, n in enumerate(sequence) for m in sequence[i:])
