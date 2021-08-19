def covered_pawns(pawns):
    covered = 0
    for pos in pawns:
        if chr(ord(pos[0]) + 1) + str(int(pos[1]) - 1) in pawns or chr(ord(pos[0]) - 1) + str(int(pos[1]) - 1) in pawns:
            covered += 1
    return covered
