def chess_board_cell_color(c1, c2):
    return isWhite(c1) == isWhite(c2)


def isWhite(c):
    i = ('ABCDEFGH'.index(c[0]) + 1) % 2
    return i != 0 if int(c[1]) % 2 == 0 else i == 0
