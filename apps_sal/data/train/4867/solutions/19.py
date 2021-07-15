def chess_board_cell_color(cell1, cell2):
    strings = 'ABCDEFG'
    ce1 = 0
    ce2 = 0
    for i, let in enumerate(strings):
        if let == cell1[0]:
            ce1 = i+1
        if let == cell2[0]:
            ce2 = i+1
    if ((int(cell1[1])%2) == 0 and (ce1%2) == 0) or ((int(cell1[1])%2) == 1 and (ce1%2) != 0):
        color1 = 'r'
    else:
        color1 = 'w'
    if ((int(cell2[1])%2) == 0 and (ce2%2) == 0) or ((int(cell2[1])%2) == 1 and (ce2%2) != 0):
    #if ((int(cell2[1])%2) == 0 and ce2%2 == 0) or ((int(cell2[1])%2) == 1 and ce2%2 != 0):
        color2 = 'r'
    else:
        color2 = 'w'
    if color1 == color2:
        return True
    else:
        return False

