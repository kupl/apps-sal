def find_missing_number(sequence):
    if not sequence.replace(' ', '').isdigit():
        return 1 * bool(sequence)
    sequence = set((int(a) for a in sequence.split(' ')))
    missing = list(set(range(1, max(sequence))) - sequence)
    return 0 if not missing else missing[0]
