def chess_board_cell_color(c1, c2):
    return len(set((x[1] in '1357' if x[0] in 'ACEG' else x[1] in '2468' for x in [c1, c2]))) == 1
