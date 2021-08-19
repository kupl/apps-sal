def find_missing_number(sequence):
    if not sequence:
        return 0
    if sequence.replace(' ', '').isnumeric():
        sequence = sorted((int(i) for i in sequence.split(' ')))
        for i in range(1, sequence[len(sequence) - 1]):
            if i not in sequence:
                return i
        return 0
    return 1
