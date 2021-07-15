def find_missing_number(sequence):
    if len(sequence) == 0:
        return 0
    sequence = sequence.split()
    int_sequence = sorted(int(d) for d in sequence if d.isdigit())
    if len(sequence) != len(int_sequence):
        return 1
    control = [n for n in range(1, int_sequence[-1]+1)]
    for n, j in zip(control, int_sequence):
        if n != j:
            return n
    return 0
