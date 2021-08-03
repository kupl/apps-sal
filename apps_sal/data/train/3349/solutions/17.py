def find_missing_number(seq):
    try:
        seq = [int(a) for a in seq.split()]
    except ValueError:
        return 1
    for num in range(1, len(seq) + 1):
        if num not in seq:
            return num
    return 0
