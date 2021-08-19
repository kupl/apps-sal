def find_missing_number(sequence):
    if len(sequence) < 1:
        return 0
    try:
        sequence = [int(item) for item in sequence.split(sep=' ')]
    except ValueError:
        return 1
    else:
        for item in range(1, len(sequence) + 1):
            if item not in sequence:
                return item
    return 0
