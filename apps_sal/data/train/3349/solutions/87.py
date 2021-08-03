def find_missing_number(sequence):
    if not sequence:
        return 0
    l = sequence.split()
    sd = "".join(l)
    if sd.isdigit():
        l = [int(i) for i in l]
        for idx, el in enumerate(sorted(l), 1):
            if el != idx:
                return idx
        return 0
    return 1
