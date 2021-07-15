def check(c):
    if c[0] in "ACEG":
        if int(c[1]) % 2 == 0:
            return "W"
        else:
            return "B"
    elif c[0] in "BDFH":
        if int(c[1]) % 2 == 0:
            return "B"
        else:
            return "W"
    
def chess_board_cell_color(cell1, cell2):
    return check(cell1) == check(cell2)


