def Color(cell):
    return ('ABCDEFGH'.index(cell[0]) + '12345678'.index(cell[1])) % 2


def chess_board_cell_color(cell1, cell2):
    return Color(cell1) == Color(cell2)
