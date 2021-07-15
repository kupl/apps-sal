def find_missing_number(sequence):
    try:
        seq = [int(e) for e in sequence.split()]
    except ValueError:
        return 1
    for i in range(1, len(seq) + 1):
        if i not in seq:
            return i
    return 0
