import copy


def knights_tour(start, size):
    print(start, size)
    '\n    Finds a knight\'s tour from start position visiting every\n    board position exactly once.\n\n    A knight may make any "L" move which is valid in chess. That is:\n    any rotation of "up 1 over 2" or "up 2 over 1". The problem\n    description has a full explanation of valid moves.\n\n    Arguments:\n        start - (row, col) starting position on board.\n        size - number of rows in the square board.\n\n    Returns:\n        List of positions beginning with the start position\n        which constitutes a valid tour of the board; visiting\n        each position exactly once.\n    '
    board = []
    for i in range(size):
        board.append([0 for _ in range(size)])
    board[start[0]][start[1]] = 1
    (_, result) = tour(board, start[0], start[1], 2)
    return list(reversed(result))


def tour(board, last_x, last_y, move_number):
    if move_number == len(board) ** 2 + 1:
        return (True, [(last_x, last_y)])
    x = [2, 1, -1, -2, -2, -1, 1, 2]
    y = [1, 2, 2, 1, -1, -2, -2, -1]
    moves = list(zip(x, y))
    legal_moves = [(x, y) for (x, y) in moves if is_move_legal(board, len(board), last_x + x, last_y + y)]
    priorities = dict()
    for move in legal_moves:
        priorities[move] = count_possible_moves(board, last_x + move[0], last_y + move[1])
    for (move, _) in sorted(list(priorities.items()), key=by_value):
        board_copy = copy.deepcopy(board)
        board_copy[last_x][last_y] = move
        (result, trace) = tour(board_copy, last_x + move[0], last_y + move[1], move_number + 1)
        if result:
            return (True, trace + [(last_x, last_y)])
    return (False, None)


def is_move_legal(board, size, new_x, new_y):
    return size > new_x >= 0 and size > new_y >= 0 and (board[new_x][new_y] == 0)


def count_possible_moves(board, cx, cy):
    x = [2, 1, -1, -2, -2, -1, 1, 2]
    y = [1, 2, 2, 1, -1, -2, -2, -1]
    moves = list(zip(x, y))
    return sum([1 for (nx, ny) in moves if is_move_legal(board, len(board), cx + nx, cy + ny)])


def by_value(item):
    return item[1]


def __starting_point():
    print(knights_tour((0, 2), 6))


__starting_point()
