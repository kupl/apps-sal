def find_missing_number(sequence):
    try:
        for (idx, x) in enumerate(sorted(map(int, sequence.split()))):
            if int(x) != idx + 1:
                return idx + 1
    except:
        return 1
    return 0
