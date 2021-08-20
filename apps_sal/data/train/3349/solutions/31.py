def find_missing_number(sequence):
    if sequence == '':
        return 0
    if not sequence.isdigit or any((c.isalpha() for c in sequence)) or '_' in sequence:
        return 1
    s = sorted((int(num) for num in sequence.split(' ')))
    if s[-1] == len(s) and s[0] == 1:
        return 0
    for i in range(len(s)):
        if s[i] != i + 1:
            return i + 1
