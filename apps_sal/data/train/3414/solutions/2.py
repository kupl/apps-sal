def reversi_row(moves):
    row = ['.'] * 8
    for (turn, move) in enumerate(moves):
        tile = '*O'[turn % 2]
        row[move] = tile
        for direction in (-1, 1):
            other = move + direction
            while 0 <= other < 8 and row[other] != '.':
                if row[other] == tile:
                    break
                other += direction
            else:
                other = move
            row[move:other:direction] = [tile] * abs(move - other)
    return ''.join(row)
