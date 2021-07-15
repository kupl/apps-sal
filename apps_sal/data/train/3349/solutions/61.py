def find_missing_number(sequence):
    if not sequence:
        return 0
    sequence = sequence.split()
    for item in sequence:
        if not item.isdigit():
            return 1
    sequence = sorted(list(map(int, sequence)))
    proper_seq = range(1, len(sequence) + 1)
    for x, y in zip(sequence, proper_seq):
        if x != y:
            return y
    return 0
