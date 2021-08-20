def whose_turn(positions):
    return sum((ord(file) + ord(rank) for (file, rank) in positions.split(';'))) % 2 == 0
