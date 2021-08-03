def find_missing_number(sequence):
    s = sequence.split()
    try:
        s = [int(x) for x in s]
    except ValueError:
        return 1
    s.sort()
    for i in range(len(s)):
        if s[i] != i + 1:
            return i + 1
    return 0
