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
    def next_moves(pos):
        eight_moves = ((pos[0] + i, pos[1] + j) for (i, j) in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)))
        return [(r, c) for (r, c) in eight_moves if 0 <= r and r < size and 0 <= c and c < size and board[r][c]]

    def solve(pos):
        if len(moves) == size * size:
            return moves
        for r, c in sorted(next_moves(pos), key=lambda m: len(next_moves(m))):
            board[r][c] = False
            moves.append((r, c))
            try:
                return solve((r, c))
            except ValueError:
                board[r][c] = True
                moves.pop()
        raise ValueError('Not possible')

    board = [[True] * size for _ in xrange(size)]
    board[start[0]][start[1]] = False
    moves = [start]

    return solve(start)
