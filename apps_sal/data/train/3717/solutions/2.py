def covered_pawns(pawns):
    return sum((any((chr(ord(c) + delta) + chr(ord(r) - 1) in pawns for delta in [-1, 1])) for (c, r) in pawns))
