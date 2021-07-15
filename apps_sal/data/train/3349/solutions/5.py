def find_missing_number(sequence):
    if not sequence:
        return 0
    if not sequence.replace(" ", "").isnumeric():
        return 1
    seq = list(map(int, sequence.split(" ")))
    result = [number for number in [x for x in range(1, max(seq))] if number not in seq]
    return 0 if not result else result[0]
