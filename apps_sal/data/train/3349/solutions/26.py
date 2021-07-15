def find_missing_number(sequence):
    if len(sequence) == 0:
        return 0
    else:
        try:
            x = [int(i) for i in sequence.split()]
        except:
            return 1
        missing = set(range(1,max(x)+1)) - set(x)
        if len(missing) == 0:
            return 0
        else:
            return list(missing)[0]
