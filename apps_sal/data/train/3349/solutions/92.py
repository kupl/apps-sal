def find_missing_number(sequence):
    if sequence:
        for i in sequence:
            if i not in '0123456789 ':
                return 1
                break
        strArr = sequence.split()
        Arr = [int(i) for i in strArr]
        Arr.sort()
        check = [i for i in range(1, max(Arr) + 1)]
        for i in check:
            if i not in Arr:
                return i
                break
        return 0
    else:
        return 0
