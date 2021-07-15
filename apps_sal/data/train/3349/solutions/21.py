def find_missing_number(sequence):
    v = 1
    try:
        for n in sorted(map(int, sequence.split())):
            if n != v:
                return v
            v += 1
    except:
        return 1
    return 0
