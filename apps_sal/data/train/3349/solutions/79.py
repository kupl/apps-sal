def find_missing_number(sequence):
    # your code here
    if not sequence:
        return 0
    try:
        list = [int(a) for a in sequence.split()]
        for i in range(1, len(list) + 1):
            if i not in list:
                return i
    except ValueError:
        return 1
    return 0
