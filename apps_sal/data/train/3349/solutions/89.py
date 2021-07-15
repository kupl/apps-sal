def find_missing_number(seq):
    if not seq:
        return 0
    try:
        numbers = sorted(map(int, seq.split(' ')))
        for i in range(len(numbers)):
            if numbers[i] != i + 1:
                return i + 1
        return 0
    except:
        return 1
