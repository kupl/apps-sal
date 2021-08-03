def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        l = [int(elem) for elem in sequence.split(' ')]
    except ValueError:
        return 1
    for i in range(1, len(l) + 1):
        if i not in l:
            return i
    return 0
