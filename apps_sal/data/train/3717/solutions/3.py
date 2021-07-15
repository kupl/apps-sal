def covered_pawns(pawns):
    count = 0
    pawn_pos = set(pawns)
    for p in pawns:
        if p[-1] != "1":
            if any(f"{chr(ord(p[0]) + i)}{int(p[1]) - 1}" in pawn_pos for i in (-1, 1)):
                count += 1
    return count

