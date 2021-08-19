def find_missing_number(sequence):
    s = sequence.split()
    if all((el.isdigit() for el in s)):
        for i in range(1, len(s) + 1):
            if str(i) not in s:
                return i
        return 0
    return 1
