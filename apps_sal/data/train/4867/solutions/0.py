def chess_board_cell_color(a, b):
    return (ord(a[0]) + int(a[1])) % 2 == (ord(b[0]) + int(b[1])) % 2
