from numpy import diagonal, rot90


def who_is_winner(pieces_position_list):
    board = [[' '] * 6 for _ in range(7)]

    def check(i, j, p):
        if p in ''.join(board[i]):
            return True
        if p in ''.join(list(zip(*board))[j]):
            return True
        if p in ''.join(diagonal(board, j - i)):
            return True
        if p in ''.join(diagonal(rot90(board), +i + j - 5)):
            return True
        return False
    id = [0] * 7
    for move in pieces_position_list:
        (i, p) = (ord(move[0]) - 65, move[2])
        j = id[i]
        (board[i][j], id[i]) = (p, j + 1)
        if check(i, j, p * 4):
            return 'Yellow' if p == 'Y' else 'Red'
    return 'Draw'
