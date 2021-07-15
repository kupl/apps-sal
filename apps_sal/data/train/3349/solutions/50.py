def find_missing_number(sequence):
    if sequence == "":
        return 0
    seq = sequence.split()
    if not ''.join(seq).isdigit():
        return 1
    seq = list(map(int, seq))
    qwe = [i for i in range(1, max(seq) + 1)]
    if len(seq) == len(qwe):
        return 0
    for i in range(1, max(seq) + 1):
        if i not in seq:
            return i
            break
