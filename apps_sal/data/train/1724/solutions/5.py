def blast_sequence(aliens, position):
    (si, sj) = position
    (rows, cols) = (si + 1, len(aliens[0]))
    board = [[[a] if a else [] for a in alien] for alien in aliens] + [[[]] * cols for c in range(rows - len(aliens))]
    count = len([a for al in aliens for (i, a) in enumerate(al) if a])
    turn = 0
    res = []
    while count > 0:
        board = move(board, rows, cols)
        if not board:
            return None
        for pi in range(rows - 2, -1, -1):
            col = board[pi][sj]
            if not col:
                continue
            if len(col) == 1:
                board[pi][sj] = []
            else:
                dead = sorted(col, key=lambda v: (abs(v), v)).pop()
                board[pi][sj].remove(dead)
            res.append(turn)
            count -= 1
            break
        turn += 1
    return res


def move(board, rows, cols):
    if any((l for l in board[-1])):
        return None
    temp = [[[] for a in row] for row in board]
    for (i, row) in enumerate(board):
        for (j, alien_list) in enumerate(row):
            if not alien_list:
                continue
            for (k, alien) in enumerate(alien_list):
                ni = i
                nj = j + alien
                if nj < 0:
                    nj = abs(nj) - 1
                    ni += 1
                    alien *= -1
                elif nj >= cols:
                    nj = cols - 1 - nj % cols
                    ni += 1
                    alien *= -1
                if ni == rows - 1:
                    return None
                temp[ni][nj].append(alien)
    return temp
