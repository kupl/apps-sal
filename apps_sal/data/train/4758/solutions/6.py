def connect_four_place(columns):
    board = [['-' for i in range(7)] for j in range(6)]
    for (turn, column) in enumerate(columns):
        for line in board:
            if line[column] == '-':
                line[column] = 'R' if turn % 2 else 'Y'
                break
    return board[::-1]
