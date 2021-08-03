def validSolution(board):
    valid = set(range(1, 10))

    for row in board:
        if set(row) != valid:
            return False

    for col in [[row[i] for row in board] for i in range(9)]:
        if set(col) != valid:
            return False

    for x in range(3):
        for y in range(3):
            if set(sum([row[x * 3:(x + 1) * 3] for row in board[y * 3:(y + 1) * 3]], [])) != valid:
                return False

    return True
