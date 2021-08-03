import math
import numpy as np

alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def queens(position, size):
    if size == 1:
        return "a1"
    if size != 10:
        x = list(range(1, size + 1))
    if size == 10:
        x = list(range(1, size))
        x.append(0)

    print(x)
    pos_step = []
    # making the board
    board = np.empty([size, size], dtype=object)
    for i in range(size):
        for j in range(size):
            board[i, j] = str(str(alph[j]) + str(x[-i - 1]))
    print(board)
    board_states = list(np.empty([size, size], dtype=object))

    # position coordinates
    pos = list(np.where(board == position))
    print(pos)
    if len(pos[0]) == 0:
        return None

    # first queen
    new_queen(position, size, board, board_states, pos_step, x)
    board_states.append(np.copy(board))

    w_col = list(range(size))
    w_col.remove(pos[1])
    col_steps = ([w_col.copy()])

    find_spot(size, board, board_states, pos_step, w_col, col_steps, x)
    output = (str(",".join(sorted(pos_step))))
    return output


def new_queen(new_position, size, board, board_states, pos_step, x):
    pos_step.append(new_position)

    pos = list(np.where(board == new_position))

    # row
    for i in range(size):
        board[i, pos[1]] = "  "

    # column
    for i in range(size):
        board[pos[0], i] = "  "

    # diagonal1
    if pos[1] - pos[0] >= 0:
        np.fill_diagonal(board[:, int(pos[1] - pos[0]):], "  ")
    else:
        np.fill_diagonal(board[int(pos[0] - pos[1]):], "  ")
    # diagonal2
    if pos[0] + pos[1] >= size:
        np.fill_diagonal(board[int(pos[1] - (size - pos[0]) + 1):, ::-1], "  ")
    else:
        np.fill_diagonal(np.fliplr(board[:, :int(pos[1] + pos[0] + 1)]), "  ")

    board[tuple(pos)] = new_position
    board_states.append(np.copy(board))


def find_spot(size, board, board_states, pos_step, w_col, col_steps, x):
    fill = 0
    i = w_col[0]
    for j in range(size):
        if board[j, i] == "  " or board[j, i] == "# ":
            continue

        pos_found = str(str(alph[i]) + str(x[-j - 1]))
        new_queen(pos_found, size, board, board_states, pos_step, x)
        fill = 1
        break

    if fill == 1:
        if len(pos_step) != size:
            w_col.remove(i)
            col_steps.append(w_col.copy())
            print(col_steps)
            find_spot(size, board, board_states, pos_step, w_col, col_steps, x)
            return

    else:
        del board_states[-1]
        del col_steps[-1]
        board = np.copy(board_states[-1])
        w_col = col_steps[-1].copy()
        d_spot = list(np.where(board == pos_step[-1]))
        board[d_spot[0], d_spot[1]] = "# "
        del board_states[-1]
        board_states.append(np.copy(board))
        del pos_step[-1]
        find_spot(size, board, board_states, pos_step, w_col, col_steps, x)
        return
