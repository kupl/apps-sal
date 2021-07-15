def chess_board_cell_color(cell1, cell2):
    file1 = cell1[0]
    rank1 = cell1[1]
    
    file2 = cell2[0]
    rank2 = cell2[1]
    
    row = abs(ord(file1) - ord(file2))
    col = abs(int(rank1) - int(rank2))
    
    same_color = (row + col) % 2 == 0
    
    return same_color
