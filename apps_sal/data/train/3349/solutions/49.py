def find_missing_number(seq):
    if not seq:
        return 0
    elif not seq.replace(' ', '').isdecimal():
        return 1
    else:
        seq = set(map(int, seq.split()))
        full = set(range(1, max(seq) + 1))
        return 0 if seq == full else min(full - seq)
