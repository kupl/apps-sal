def whose_turn(positions):
    return sum((ord(c) for c in positions.replace(';', ''))) & 1 == 0
