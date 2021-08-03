def find_missing_number(sequence):
    missing = []
    l = sequence.split()
    for i in range(1, len(l) + 1):
        if not l[i - 1].isdigit():
            return 1
        if str(i) not in l:
            missing.append(i)
    return min(missing) if missing else 0
