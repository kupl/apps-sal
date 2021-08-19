def chess_board_cell_color(cell1, cell2):
    dark = ['A1', 'C1', 'E1', 'G1', 'B2', 'D2', 'F2', 'H2', 'A3', 'C3', 'E3', 'G3', 'B4', 'D4', 'F4', 'H4', 'A5', 'C5', 'E5', 'G5', 'B6', 'D6', 'F6', 'H6', 'A7', 'C7', 'E7', 'G7', 'B8', 'D8', 'F8', 'H8']
    x = 0
    y = 0
    if cell1 in dark:
        x = 1
    if cell2 in dark:
        y = 1
    if x == y:
        return True
    else:
        return False
