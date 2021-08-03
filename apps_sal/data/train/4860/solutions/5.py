def amidakuji(board):
    li = [0] * (len(board[0]) + 1)
    for i in range(len(board[0]) + 1):
        c = i
        for k in range(len(board)):
            if int(board[k][c]) if c < len(board[0]) else 0:
                c += 1
            elif int(board[k][c - 1]) if c > 0 else 0:
                c -= 1
        li[c] = i
    return li
