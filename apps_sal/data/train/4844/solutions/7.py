def get_password(grid, directions):
    axis = {'left': -1, 'leftT': -1, 'right': +1, 'rightT': +1}
    ordinate = {'up': -1, 'upT': -1, 'down': +1, 'downT': +1}
    pwd = ''
    for ele in grid:
        if 'x' in ele:
            row_index, column_index = grid.index(ele), ele.index('x')
            break

    for direction in directions:
        if 't' in direction:
            column_index += axis[direction]
            if 'T' in direction:
                pwd += grid[row_index][column_index]
        else:
            row_index += ordinate[direction]
            if 'T' in direction:
                pwd += grid[row_index][column_index]
    return pwd
