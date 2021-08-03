def knight(p1, p2):
    pos = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    p1 = [pos[p1[0]] - 1, int(p1[1]) - 1]
    p2 = [pos[p2[0]] - 1, int(p2[1]) - 1]
    moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    board = []
    for i in range(8):
        board.append([0, 0, 0, 0, 0, 0, 0, 0])
    board[p1[1]][p1[0]] = 1
    while True in [0 in ii for ii in board]:
        for j in range(8):
            for k in range(8):
                for i in moves:
                    new = [j + i[0], k + i[1]]
                    if new[0] in range(8) and new[1] in range(8) and new != p1 and board[k][j] != 0:
                        if board[new[1]][new[0]] == 0:
                            board[new[1]][new[0]] = board[k][j] + 1
                        else:
                            board[new[1]][new[0]] = min(board[k][j] + 1, board[new[1]][new[0]])
    return board[p2[1]][p2[0]] - 1
