def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for i, x in enumerate(sequence):
        for y in sequence[i + 1:]:
            if x > y:
                count += 1
    return count
