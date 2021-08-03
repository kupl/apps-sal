from functools import reduce


def reversi_row(moves):
    return ''.join(reduce(lambda board, x: play(board, x[1], 'O' if x[0] % 2 else '*'), enumerate(moves), ['.'] * 8))


def play(board, position, pawn):
    board[position] = pawn
    opp = 'O' if pawn == '*' else '*'
    after = next((x for x in [opp * i + pawn for i in range(6)] if ''.join(board[position + 1:]).startswith(x)), None)
    if after:
        board[position + 1:position + len(after)] = [pawn] * (len(after) - 1)
    before = next((x for x in [pawn + opp * i for i in range(6)] if ''.join(board[:position]).endswith(x)), None)
    if before:
        board[position - len(before):position] = [pawn] * len(before)
    return board
