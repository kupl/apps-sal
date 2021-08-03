def find_missing_number(sequence):
    if sequence == '':
        return 0
    if any(not x.isdigit() for x in sequence.split(' ')):
        return 1
    s = sorted(list(map(int, sequence.split(' '))))
    if s == list(range(1, max(s) + 1)):
        return 0
    else:
        return min(i for i in range(1, max(s) + 1) if i not in s)
