def find_missing_number(sequence):
    sequence = sequence.split()
    if any((not n.isdigit() for n in sequence)):
        return 1
    sequence = sorted((int(n) for n in sequence))
    for (i, n) in enumerate(sequence, 1):
        if int(n) != i:
            return i
    return 0
