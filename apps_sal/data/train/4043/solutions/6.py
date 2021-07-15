from itertools import combinations

def calc(game_map):
    """ A state is denoted a NE-SW diagonal of :game_map: and two different cells contained in it.        
        Its key is a triplet (diagonal, row_cell_1, row_cell_2), where holds the invariant
        diagonal == row_cell_1 + column_cell_1 == row_cell_2 + column_cell_2
        Its value is the sum of the points scored by respective paths from the top left to the cells.
    """
    rows = len(game_map)
    cols = len(game_map[0])
    
    states = {
        (1, 0, 1): game_map[0][0] + game_map[0][1] + game_map[1][0]
        }
    
    state_keys = []
    for diagonal in range(2, rows + cols - 1):
        min_row = max(0, diagonal - cols + 1)
        max_row = min(rows - 1, diagonal)
        row_codes = range(min_row, max_row + 1)
        for (row_cell_1, row_cell_2) in combinations(row_codes, 2):
            state_keys.append((diagonal, row_cell_1, row_cell_2))

    for (diagonal, row_cell_1, row_cell_2) in state_keys:       
        prev_values = []
        
        # Both paths downwards
        if row_cell_1 > 0:
            prev_values.append(states[(diagonal - 1, row_cell_1 - 1, row_cell_2 - 1)])
            
        # Cell 1 downwards and cell 2 rightwards
        if row_cell_1 > 0 and row_cell_2 < diagonal:
            prev_values.append(states[(diagonal - 1, row_cell_1 - 1, row_cell_2)])
            
        # Cell 1 rightwards and cell 2 downwards. Excluded the case
        # where both paths come from a common cell for efficiency.
        if row_cell_2 > row_cell_1 + 1:
            prev_values.append(states[(diagonal - 1, row_cell_1, row_cell_2 - 1)])
            
        # Both paths rightwards
        if row_cell_2 < diagonal:
            prev_values.append(states[(diagonal - 1, row_cell_1, row_cell_2)])
            
        prev_value = max(prev_values)
        col_cell_1 = diagonal - row_cell_1
        col_cell_2 = diagonal - row_cell_2
        new_value = prev_value + game_map[row_cell_1][col_cell_1] + game_map[row_cell_2][col_cell_2]
        states[(diagonal, row_cell_1, row_cell_2)] = new_value
    
    final_diagonal = (rows + cols - 3, rows - 2, rows - 1)
    return states[final_diagonal] + game_map[rows - 1][cols - 1]
