def find_missing_number(sequence):
    try:
        a = set(map(int, sequence.split()))
        try:
            return min(set(range(1, max(a) + 1)) - set(a))
        except:
            return 0
    except:
        return 1
