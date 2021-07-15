from itertools import cycle

def chess_board(rows, columns):
    result = []
    for i in range(rows):
        grida = cycle(['O', 'X'])
        gridb = cycle(['X', 'O'])
        result.append([next(gridb) if i % 2  else next(grida) for x in range(columns)])
    return result
