def pawn_move_tracker(moves):
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]]

    for i in range(len(moves)):
        row = abs(int(moves[i][1]) - 8) if moves[i][1] != 'x' else abs(int(moves[i][3]) - 8)
        col = ord(moves[i][0]) - 97 if moves[i][1] != 'x' else ord(moves[i][2]) - 97
        white_turn = bool((i % 2) == 0)
        piece1 = "P" if white_turn == True else "p"
        piece2 = "p" if white_turn == True else "P"
        back1 = row + 1 if white_turn == True else row - 1
        back2 = row + 2 if white_turn == True else row - 2
        current_row, current_col = back1, col

        if 'x' in moves[i] and board[row][col] == piece2:
            current_col = ord(moves[i][0]) - 97
            if board[back1][current_col] != piece1:
                return f"{moves[i]} is invalid"
        elif board[back1][col] == "." and board[back2][col] == piece1:
            if (white_turn == True and back2 == 6) or (white_turn == False and back2 == 1):
                current_row = back2
            else:
                return f"{moves[i]} is invalid"
        elif board[back1][col] != piece1 or board[row][col] != ".":
            return f"{moves[i]} is invalid"

        board[current_row][current_col] = "."
        board[row][col] = piece1

    return board
