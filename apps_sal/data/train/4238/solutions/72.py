def squares_needed(grains):
    s = 0
    cells = 0
    grains_in_cell = 1
    while s < grains:
      s += grains_in_cell 
      grains_in_cell *= 2
      cells += 1
    return cells
