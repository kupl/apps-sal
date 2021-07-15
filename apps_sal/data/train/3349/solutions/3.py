def find_missing_number(sequence):
    try:
        seq = set(map(int, sequence.split()))
        return (set(range(1, 1 + max(seq, default = 0))) - seq or {0}).pop()
    except:
        return 1
