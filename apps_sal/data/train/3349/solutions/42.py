def find_missing_number(sequence):
    try:
        l = [int(i) for i in sequence.split()]
        l.sort()
        for i in range(1, l[-1]):
            if i not in l:
                return i
        else:
            return 0
    except:
        return 1 if sequence != '' else 0
