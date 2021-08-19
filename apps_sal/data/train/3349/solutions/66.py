def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        sequence = set(sorted((int(s) for s in sequence.split())))
        diff = set(range(1, max(sequence) + 1)) - sequence
        if not diff:
            return 0
        return min(diff)
    except:
        return 1
