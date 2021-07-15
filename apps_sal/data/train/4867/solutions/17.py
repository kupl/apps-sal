def chess_board_cell_color(cell1, cell2):
    board = {
        'A': 'BW'*4, 'B': 'WB'*4, 'C': 'BW'*4, 'D': 'WB'*4,
        'E': 'BW'*4, 'F': 'WB'*4, 'G': 'BW'*4, 'H': 'WB'*4,
    }
    
    return board[cell1[0]][int(cell1[1])-1] == board[cell2[0]][int(cell2[1])-1]
