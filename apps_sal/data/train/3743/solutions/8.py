def chess_board(rows, columns):
    line = ["X", "O"] * columns
    return [line[:columns] if r % 2 else line[1:columns+1] for r in range(rows)]
