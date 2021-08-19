from itertools import product


def get_pos(coord):
    x = ord(coord[0]) - ord('a')
    y = int(coord[1]) - 1
    return [y, x]


def place_pieces(board, king, amazon, connected):
    coord_king = get_pos(king)
    board[coord_king[0]][coord_king[1]] = 8
    coord_amazon = get_pos(amazon)
    board[coord_amazon[0]][coord_amazon[1]] = 9
    if coord_king[0] - 1 <= coord_amazon[0] <= coord_king[0] + 1 \
            and coord_king[1] - 1 <= coord_amazon[1] <= coord_king[1] + 1:
        connected[0] = 1
    mark_attacked_squares(board, coord_king, coord_amazon)


def mark_attacked_squares(board, coord_king, coord_amazon):
    mark_queen(board, coord_amazon)
    mark_knight(board, coord_amazon)
    mark_king(board, coord_king)
    board[coord_amazon[0]][coord_amazon[1]] = 9


def mark_king(board, coord_king):
    y = coord_king[0]
    x = coord_king[1]
    for i in product([-1, 0, 1], repeat=2):
        if 0 <= y + i[0] < 8 and 0 <= x + i[1] < 8:
            board[y + i[0]][x + i[1]] = 3


def mark_knight(board, coord_amazon):
    y = coord_amazon[0]
    x = coord_amazon[1]
    for i in product([-2, -1, 1, 2], repeat=2):
        if 0 <= y + i[0] < 8 and 0 <= x + i[1] < 8:
            if board[y + i[0]][x + i[1]] == 0:
                board[y + i[0]][x + i[1]] = 2


def mark_queen(board, coord_amazon):
    y = coord_amazon[0]
    x = coord_amazon[1]
    while y >= 0:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        y -= 1
    y = coord_amazon[0]
    while y < 8:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        y += 1
    y = coord_amazon[0]
    while x >= 0:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        x -= 1
    x = coord_amazon[1]
    while x < 8:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        x += 1
    x = coord_amazon[1]
    while x >= 0 and y >= 0:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        x -= 1
        y -= 1
    y = coord_amazon[0]
    x = coord_amazon[1]
    while x < 8 and y >= 0:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        x += 1
        y -= 1
    y = coord_amazon[0]
    x = coord_amazon[1]
    while x >= 0 and y < 8:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        x -= 1
        y += 1
    y = coord_amazon[0]
    x = coord_amazon[1]
    while x < 8 and y < 8:
        if board[y][x] == 0:
            board[y][x] = 2
        if board[y][x] == 8:
            break
        x += 1
        y += 1
    y = coord_amazon[0]
    x = coord_amazon[1]


def check_safe(board, y, x, connected):
    for i in product([-1, 0, 1], repeat=2):
        if 0 <= y + i[0] < 8 and 0 <= x + i[1] < 8:
            if not (i[0] == 0 and i[1] == 0) and \
                (board[y + i[0]][x + i[1]] == 0 or
                 (connected[0] == 0 and board[y + i[0]][x + i[1]] == 9)):
                return 1
    return 0


def count_states(board, connected):
    stalemate = check = checkmate = safe = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == 0:
                if check_safe(board, y, x, connected) == 1:
                    safe += 1
                else:
                    stalemate += 1
            elif board[y][x] == 2:
                if check_safe(board, y, x, connected) == 0:
                    checkmate += 1
                else:
                    check += 1
    return [checkmate, check, stalemate, safe]


def amazon_check_mate(king, amazon):
    board = [[0 for i in range(8)] for j in range(8)]
    connected = [1]
    connected[0] = 0
    place_pieces(board, king, amazon, connected)
    return count_states(board, connected)
    # 0 = safe
    # 8 = whiteking
    # 9 = amazon
    # 2 = attacked
    # 3 = black king can't be here
