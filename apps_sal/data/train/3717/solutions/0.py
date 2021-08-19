def covered_pawns(pawns):
    pawns = set(pawns)
    return len({p for p in pawns for (x, y) in [map(ord, p)] if {chr(x - 1) + chr(y - 1), chr(x + 1) + chr(y - 1)} & pawns})
