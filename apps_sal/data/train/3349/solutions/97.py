def find_missing_number(sequence):
    if sequence == '':
        return 0
    sequence = sequence.split()
    if any((not x.isdigit() for x in sequence)):
        return 1
    sequence = set((int(x) for x in sequence))
    if sequence == set(range(1, max(sequence) + 1)):
        return 0
    else:
        return min(set(range(1, max(sequence) + 1)).difference(sequence))
