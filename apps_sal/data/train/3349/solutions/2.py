def find_missing_number(sequence):
    try:
        sequence = [int(n) for n in sequence.split()]
    except ValueError:
        return 1
    for (i, n) in enumerate(sorted(sequence)):
        if n != i + 1:
            return i + 1
    return 0
