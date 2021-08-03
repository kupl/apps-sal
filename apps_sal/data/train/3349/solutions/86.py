def find_missing_number(sequence):
    s = sequence.split()
    if s == []:
        return 0
    try:
        s = list(map(int, s))
    except:
        return 1
    for i in range(1, max(s) + 1):
        if i not in s:
            return i
    return 0
