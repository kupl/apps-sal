def squares_needed(grains):
    s = 0
    cells = 0
    gr_in_cell = 1
    while s < grains: 
        s = s + gr_in_cell
        gr_in_cell *= 2
        cells += 1 
    return cells
