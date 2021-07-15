def find_missing_number(sequence):
    if not sequence: return 0
    try: sequence = [int(el) for el in sequence.split(" ")]
    except: return 1
    sequence.sort()
    if sequence[0] != 1: return 1
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1] + 1: return sequence[i-1] + 1
    return 0

