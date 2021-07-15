def find_missing_number(sequence):
    if len(sequence) == 0:
        return 0
    l = sequence.split()
    try:
        l = list(map(int, l))
        s1 = set(l)
        s2 = list(range(1, max(l)+1))
        s2 = set(s2)
        dif = s2.difference(s1)
        if len(dif) != 0:
            return next(iter(dif))
        else:
            return 0
    except ValueError:
        return 1
