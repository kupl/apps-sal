def knights_tour(start, size):
    """
    Finds a knight's tour from start position visiting every
    board position exactly once.

    A knight may make any "L" move which is valid in chess. That is:
    any rotation of "up 1 over 2" or "up 2 over 1". The problem
    description has a full explanation of valid moves.

    Arguments:
        start - (row, col) starting position on board.
        size - number of rows in the square board.

    Returns:
        List of positions beginning with the start position
        which constitutes a valid tour of the board; visiting
        each position exactly once.
    """
    def degree(p):
        adj = [(p[0] + x, p[1] + y) for x, y in directions]
        return sum([1 for x, y in adj if 0 <= x < size and 0 <= y < size and board[x][y] == -1])

    def check_board():
        return all([sq != -1 for row in board for sq in row])

    def knight_dfs(pos, cnt):
        if check_board():
            return True
        moves = filter(lambda m: 0 <= m[0] < size and 0 <= m[1] < size and board[m[0]][m[1]] == -1,
                       [(pos[0] + x, pos[1] + y) for x, y in directions])
        moves = sorted(moves, key=degree)
        for move in moves:
            board[move[0]][move[1]] = cnt
            if knight_dfs(move, cnt + 1):
                return True
            else:
                board[move[0]][move[1]] = -1

    def print_board():
        for row in board:
            print row

    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    board = [[-1] * size for _ in range(size)]
    board[start[0]][start[1]] = 0
    knight_dfs(start, 1)
    print_board()
    return sorted([(i, j) for i in range(size) for j in range(size)], key=lambda x: board[x[0]][x[1]])
