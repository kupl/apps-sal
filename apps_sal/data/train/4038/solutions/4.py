def chess_knight(cell):
    file = cell[0]
    rank = cell[1]
    if cell in ['a1', 'a8', 'h1', 'h8']:
        return 2
    if cell in ['a2', 'a7', 'b1', 'b8', 'g1', 'g8', 'h2', 'h7']:
        return 3
    if 'c' <= file <= 'f':
        if '3' <= rank <= '6':
            return 8
    if file in ['b', 'g'] and '3' <= rank <= '6':
        return 6
    if rank in ['2', '7'] and 'c' <= file <= 'f':
        return 6
    return 4
