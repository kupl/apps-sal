def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        sequence = [int(elem) for elem in sequence.split()]
    except ValueError:
        return 1
    for elem in range(1, len(sequence) + 1):
        if elem not in sequence:
            return elem
    return 0
