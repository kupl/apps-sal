MOVES = ((1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (1, 0), (-1, 0), (0, -1))


def find_empty(row, X):
    for y, spot in enumerate(row):
        if spot == 0:
            yield (X, y)


def populating_board(x, y, board):
    board[x][y] += 1
    pos = [(x, y)]

    for dx, dy in MOVES:
        c = 0
        while True:
            c += 1
            xx = x + c * dx
            yy = y + c * dy

            if not (0 <= xx < len(board) and 0 <= yy < len(board)):
                break

            if (xx, yy) != (x, y):
                board[xx][yy] += 1
                pos.append((xx, yy))

    return pos


def queens(position, size):
    board = [[0] * size for i in range(size)]
    y, x = ord(position[0]) - 97, size - (size == 10 and not int(position[1]) and 10 or int(position[1]))
    initial_X = x

    populating_board(x, y, board)
    queens = [position]

    def dfs(counter, next_X):
        nonlocal board
        if counter == size:
            return True

        while next_X > 0 and 0 not in board[next_X]:
            next_X -= 1

        while next_X < size - 1 and 0 not in board[next_X]:
            next_X += 1

        for x, y in find_empty(board[next_X], next_X):
            queens.append(chr(y + 97) + str(size - (size == 10 and not x and 10 or x)))
            to_restore = populating_board(x, y, board)

            if dfs(counter + 1, x):
                return True

            queens.pop()
            for pos_x, pos_y in to_restore:
                board[pos_x][pos_y] -= 1

    if dfs(1, x):
        return ','.join(queens)
