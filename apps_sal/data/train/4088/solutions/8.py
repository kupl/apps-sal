import numpy as np


def columnDecode(code):
    code = code.replace("R", "+")
    code = code.replace("L", "-")
    return int(code) + 4


def placePiece(colList, size, i):
    for x in range(i, size + i):
        colList[x] = 1
    return colList


def lineCheck(board):
    i = 0
    for i in range(5):
        if not all(board[:, i]):
            break
    return i


def tetris(arr):
    totalLines = 0
    board = np.zeros((9, 29), dtype="int")
    for piece in arr:
        col = columnDecode(piece[1:])
        size = int(piece[0])
        for i in range(len(board[col]) - 1, -1, -1):
            if board[col][i - 1] == 1 or i <= 0:
                try:
                    board[col] = placePiece(board[col], size, i)
                except:
                    return totalLines
                lines = lineCheck(board)
                if lines > 0:
                    board = board[:, lines:]
                    board = np.hstack((board, np.zeros((board.shape[0], lines), dtype="int")))
                    totalLines += lines
                    lines = 0
                break
    return totalLines
