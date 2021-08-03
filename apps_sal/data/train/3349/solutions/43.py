def find_missing_number(sequence):
    a = list(map(int, list(filter(str.isdigit, sequence.split()))))
    if len(sequence.split()) != len(a):
        return 1
    if a:
        for n in range(1, max(a) + 1):
            if n not in a:
                return n
    return 0
