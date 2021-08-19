def find_missing_number(sequence):
    try:
        seq = sorted((int(i) for i in sequence.split()))
    except ValueError:
        return 1
    if seq and seq[0] != 1:
        return 1
    for (idx, nr) in enumerate(seq[:-1]):
        if nr + 1 != seq[idx + 1]:
            return nr + 1
    return 0
