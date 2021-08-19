letters = {'a': ('b',), 'b': ('a', 'c'), 'c': ('b', 'd'), 'd': ('c', 'e'), 'e': ('d', 'f'), 'f': ('e', 'g'), 'g': ('f', 'h'), 'h': ('g',)}


def get_cells(pawn):
    (x, y) = pawn
    y = int(y)
    if y < 8:
        cells = [letter + str(y + 1) for letter in letters[x]]
        return cells
    return []


def covered_pawns(pawns):
    res = set()
    pawns = set(pawns)
    for pawn in pawns:
        cells = get_cells(pawn)
        for cell in cells:
            if cell in pawns:
                res.add(cell)
    return len(res)
