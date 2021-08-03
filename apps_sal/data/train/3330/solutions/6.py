def make_triangle(n, m):
    layers = layer(m - n + 1)
    if layers == False:
        return ""
    board = []
    for i in range(layers):
        board.append([""] * (i + 1))
    triangle = make(n % 10, board, 0, 0, len(board))
    return tri_print(triangle)


def layer(n):
    a = 0
    layer = 0
    for i in range(1, n):
        a += i
        layer += 1
        if a == n:
            return layer
        elif a > n:
            return False
        else:
            continue


def tri_print(board):
    sentence = ""
    for i in range(len(board)):
        sentence += " " * (len(board) - 1 - i)
        for j in range(len(board[i])):
            sentence += str(board[i][j]) + " "
        sentence = sentence[:-1] + "\n"
    return sentence[:-1]


def make(n, board, row, col, x):
    for i in range(row, x):
        if board[i][col] == "":
            board[i][col] = n
            if n == 9:
                n = 0
            else:
                n += 1
        col += 1
    for j in range(x - 1, -1, -1):
        if board[x - 1][j] == "":
            board[x - 1][j] = n
            n_col = j
            if n == 9:
                n = 0
            else:
                n += 1
    if check(board):
        return board
    for z in range(x - 1, row, -1):
        if board[z][n_col] == "":
            board[z][n_col] = n
            rw, cl = z, n_col
            if n == 9:
                n = 0
            else:
                n += 1

    if not check(board):
        return make(n, board, rw, cl, x - 1)
    return board


def check(board):
    for i in board:
        for j in i:
            if j == "":
                return False
    return True
