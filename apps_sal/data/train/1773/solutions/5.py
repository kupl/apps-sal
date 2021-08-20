from itertools import product


def validSolution(board):
    rows = board
    columns = list(map(list, list(zip(*board))))
    blocks = [[board[i][j] for (i, j) in product(range(x, x + 3), range(y, y + 3))] for (x, y) in product((0, 3, 6), repeat=2)]
    return all((sorted(line) == list(range(1, 10)) for lines in (rows, columns, blocks) for line in lines))
