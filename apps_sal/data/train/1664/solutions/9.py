import numpy as np
d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def get_area(board, x, y):
    return board[x - 1 if x - 1 >= 0 else 0:x + 2 if x + 2 <= 8 else 8, y - 1 if y - 1 >= 0 else 0:y + 2 if y + 2 <= 8 else 8]


def get_neig(board, x, y):
    rtrn = []
    if x - 1 >= 0:
        if y - 1 >= 0:
            rtrn.append(board[x - 1, y - 1])
        rtrn.append(board[x - 1, y])
        if y + 1 < 8:
            rtrn.append(board[x - 1, y + 1])
    if y - 1 >= 0:
        rtrn.append(board[x, y - 1])
    if y + 1 < 8:
        rtrn.append(board[x, y + 1])
    if x + 1 < 8:
        if y - 1 >= 0:
            rtrn.append(board[x + 1, y - 1])
        rtrn.append(board[x + 1, y])
        if y + 1 < 8:
            rtrn.append(board[x + 1, y + 1])
    return rtrn


def amazon_check_mate(king, amazon):
    print(king, amazon)
    board = np.array([['O'] * 8 for i in range(8)])
    (kingx, kingy) = (int(king[1]) - 1, d[king[0]])
    (amazonx, amazony) = (int(amazon[1]) - 1, d[amazon[0]])
    board[kingx][kingy] = 'K'
    board[amazonx][amazony] = 'A'
    subarray = get_area(board, kingx, kingy)
    for (x, y) in np.ndenumerate(subarray):
        if y == 'O':
            subarray[x] = 'N'
        if y == 'A':
            subarray[x] = 'F'
    for xy in range(amazony, 8):
        if board[amazonx, xy] == 'K':
            break
        elif board[amazonx, xy] == 'O':
            board[amazonx, xy] = 'W'
    for xy in range(amazony, -1, -1):
        if board[amazonx, xy] == 'K':
            break
        elif board[amazonx, xy] == 'O':
            board[amazonx, xy] = 'W'
    for yx in range(amazonx, 8):
        if board[yx, amazony] == 'K':
            break
        elif board[yx, amazony] == 'O':
            board[yx, amazony] = 'W'
    for yx in range(amazonx, -1, -1):
        if board[yx, amazony] == 'K':
            break
        elif board[yx, amazony] == 'O':
            board[yx, amazony] = 'W'
    diag = np.diagonal(board, amazony - amazonx)
    diag.setflags(write=True)
    if 'A' in diag:
        for di in range(np.where(diag == 'A')[0][0], len(diag)):
            if diag[di] == 'K':
                break
            if diag[di] == 'O':
                diag[di] = 'W'
        for di in range(np.where(diag == 'A')[0][0], -1, -1):
            if diag[di] == 'K':
                break
            if diag[di] == 'O':
                diag[di] = 'W'
    if 'F' in diag:
        for di in range(np.where(diag == 'F')[0][0], len(diag)):
            if diag[di] == 'K':
                break
            if diag[di] == 'O':
                diag[di] = 'W'
        for di in range(np.where(diag == 'F')[0][0], -1, -1):
            if diag[di] == 'K':
                break
            if diag[di] == 'O':
                diag[di] = 'W'
    diag2 = np.rot90(board).diagonal(-8 + amazonx + amazony + 1)
    diag2.setflags(write=True)
    if 'A' in diag2:
        for di in range(np.where(diag2 == 'A')[0][0], len(diag2)):
            if diag2[di] == 'K':
                break
            if diag2[di] == 'O':
                diag2[di] = 'W'
        for di in range(np.where(diag2 == 'A')[0][0], -1, -1):
            if diag2[di] == 'K':
                break
            if diag2[di] == 'O':
                diag2[di] = 'W'
    if 'F' in diag:
        for di in range(np.where(diag2 == 'F')[0][0], len(diag2)):
            if diag2[di] == 'K':
                break
            if diag2[di] == 'O':
                diag2[di] = 'W'
        for di in range(np.where(diag2 == 'F')[0][0], -1, -1):
            if diag2[di] == 'K':
                break
            if diag2[di] == 'O':
                diag2[di] = 'W'
    if amazonx - 2 >= 0:
        if amazony - 1 >= 0 and board[amazonx - 2, amazony - 1] == 'O':
            board[amazonx - 2, amazony - 1] = 'W'
        if amazony + 1 < 8 and board[amazonx - 2, amazony + 1] == 'O':
            board[amazonx - 2, amazony + 1] = 'W'
    if amazonx + 2 < 8:
        if amazony - 1 >= 0 and board[amazonx + 2, amazony - 1] == 'O':
            board[amazonx + 2, amazony - 1] = 'W'
        if amazony + 1 < 8 and board[amazonx + 2, amazony + 1] == 'O':
            board[amazonx + 2, amazony + 1] = 'W'
    if amazony - 2 >= 0:
        if amazonx - 1 >= 0 and board[amazonx - 1, amazony - 2] == 'O':
            board[amazonx - 1, amazony - 2] = 'W'
        if amazonx + 1 < 8 and board[amazonx + 1, amazony - 2] == 'O':
            board[amazonx + 1, amazony - 2] = 'W'
    if amazony + 2 < 8:
        if amazonx - 1 >= 0 and board[amazonx - 1, amazony + 2] == 'O':
            board[amazonx - 1, amazony + 2] = 'W'
        if amazonx + 1 < 8 and board[amazonx + 1, amazony + 2] == 'O':
            board[amazonx + 1, amazony + 2] = 'W'
    for i in range(8):
        for j in range(8):
            neigs = get_neig(board, i, j)
            if board[i, j] == 'O' and neigs.count('O') == 0:
                board[i, j] = 'S'
            if board[i, j] == 'W' and neigs.count('O') + neigs.count('A') + neigs.count('S') == 0:
                board[i, j] = 'C'
    (checkmate, warning, stalemate, safe) = (0, 0, 0, 0)
    for p in np.nditer(board):
        if p == 'C':
            checkmate += 1
        elif p == 'W':
            warning += 1
        elif p == 'S':
            stalemate += 1
        elif p == 'O':
            safe += 1
    return [checkmate, warning, stalemate, safe]
