def find_missing_number(sequence):
    if not sequence:
        return 0
    arr = sequence.split(' ')
    if any((not ch.isdigit() for ch in arr)):
        return 1
    for n in range(1, len(arr) + 1):
        if str(n) not in arr:
            return n
    return 0
