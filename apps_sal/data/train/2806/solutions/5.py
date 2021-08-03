def whose_turn(positions):
    a = [int(p, 19) & 1 for p in positions.split(';')]
    return len(set(a[:2])) == len(set(a[2:]))
