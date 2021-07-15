def chess_board_cell_color(cell1, cell2):
    return get_colour(cell1) == get_colour(cell2)
            
def get_colour(cell):
    letters = "ABCDEFGH"
    if letters.index(cell[0]) % 2 == 0:
        if int(cell[1]) % 2 == 1:
            return 'b'
        else:
            return 'w'
    else:
        if int(cell[1]) % 2 == 1:
            return 'w'
        else:
            return 'b'
