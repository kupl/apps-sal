def bingo(card, numbers):
    card = card[1:]
    indexes = {str(x): (i, j) for (i, row) in enumerate(card) for (j, x) in enumerate(row)}
    board = [[0] * 5 for _ in range(5)]
    for n in numbers + [' FREE SPACE']:
        try:
            (i, j) = indexes[n[1:]]
            board[i][j] = 1
        except KeyError:
            pass
    return any((sum(row) == 5 for row in board)) or any((sum(row) == 5 for row in zip(*board))) or all((board[i][i] for i in range(5))) or all((board[i][4 - i] for i in range(5)))
