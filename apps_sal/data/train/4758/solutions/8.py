COLUMNS = 7
ROWS = 6


def connect_four_place(columns):
    board = [['-'] * COLUMNS for row in range(ROWS)]
    height = [0] * COLUMNS
    for (i, column) in enumerate(columns):
        if i % 2 == 0:
            player = 'Y'
        else:
            player = 'R'
        board[height[column]][column] = player
        height[column] += 1
    return board[::-1]
