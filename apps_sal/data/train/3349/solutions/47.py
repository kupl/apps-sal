def find_missing_number(sequence: str):
    if not sequence:
        return 0
    try:
        sequence = [int(i) for i in sequence.split(' ')]
    except:
        return 1
    for i in range(1, max(sequence) + 1):
        if i not in sequence:
            return i
    return 0
