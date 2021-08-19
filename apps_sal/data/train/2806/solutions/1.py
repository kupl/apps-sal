def whose_turn(positions):
    return sum((ord(c) for c in positions)) & 1 == 1
