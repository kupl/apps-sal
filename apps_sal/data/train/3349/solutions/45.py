def find_missing_number(sequence):
    if sequence == "":
        return 0
    try:
        seq = sorted([int(s) for s in sequence.split(' ')])
    except:
        return 1

    a = list(range(1, seq[-1] + 1))
    return 0 if seq == a else (list(set(a) - set(seq)))[0]
