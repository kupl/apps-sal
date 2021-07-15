from collections import defaultdict


def count(chessBoard):
    result = defaultdict(int)
    n = len(chessBoard)
    for i in range(1, n):
        for j in range(1, n):
            chessBoard[i][j] = chessBoard[i][j] * (min(chessBoard[i-1][j], chessBoard[i][j-1], chessBoard[i-1][j-1]) + 1)
    for i in range(1, n):
        for j in range(1, n):
            if chessBoard[i][j] > 1:
                for k in range(2, chessBoard[i][j] + 1):
                    result[k] += 1
    return dict(result)
