import string


def vertical_win(game_board_matrix):
    win = 0
    for x_value in range(0, 7):
        coloumn = [game_board_matrix[i][x_value] for i in range(0, 6)]
        i = 0
        while i < 3:
            row4 = coloumn[i:i + 4]
            i += 1
            if row4.count('R') == 4:
                win = 1
            if row4.count('Y') == 4:
                win = 1
    if win == 1:
        return True
    elif win == 0:
        return False


def diagonal_left_win(matrix):
    win = 0
    for height_level in range(2, -1, -1):
        for x in range(6, 2, -1):
            diagonal = [matrix[height_level + offset][x - offset] for offset in range(0, 4)]
            if diagonal.count('R') == 4:
                win = 1
            if diagonal.count('Y') == 4:
                win = 1
    return win


def diagonal_right_win(matrix):
    win = 0
    for height_level in range(2, -1, -1):
        for x in range(0, 4, 1):
            diagonal = [matrix[height_level + offset][x + offset] for offset in range(0, 4)]
            if diagonal.count('R') == 4:
                win = 1
            if diagonal.count('Y') == 4:
                win = 1
    return win


def horizontal_win(matrix):
    win = 0
    for row in matrix:
        i = 0
        while i < 4:
            row4 = row[i:i + 4]
            i += 1
            if row4.count('R') == 4:
                win = 1
            if row4.count('Y') == 4:
                win = 1
    if win == 1:
        return True
    elif win == 0:
        return False


def who_is_winner(pieces_position_list):
    heigth_list = [5, 5, 5, 5, 5, 5, 5]
    w, h = 7, 6
    game_board = [[0 for x in range(w)] for y in range(h)]
    move_dict = {}
    letters = list(string.ascii_uppercase)[0:7]
    for letter, i in enumerate(letters):
        move_dict[i] = letter

    parsed_moves = [parsed_move.split("_") for parsed_move in pieces_position_list]
    converted_moves = [[move_dict[move[0]], move[1]] for move in parsed_moves]
    for move in converted_moves:
        x_coordinate, colour = move
        game_board[heigth_list[x_coordinate]][x_coordinate] = colour[0]
        if heigth_list[x_coordinate] > 0:
            heigth_list[x_coordinate] = heigth_list[x_coordinate] - 1
        if horizontal_win(game_board) or vertical_win(game_board) or diagonal_left_win(game_board) or diagonal_right_win(game_board):
            return colour
    diagonal_left_win(game_board)
    return "Draw"
