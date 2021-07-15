def find_missing_number(sequence):
    try: l = sorted([int(x) for x in sequence.split()])
    except: return 1
    for x, y in zip(l, range(1, len(l) + 1)):
        if y != x:
            return y
    return 0
