def peak_height(mountain):
    points = { (row,col) for row,lst in enumerate(mountain) for col in range(len(lst)) if lst[col] == '^' }
    height = 0
    while points:
        points -= { (row,col) for row,col in points if { (row-1,col), (row+1,col), (row,col-1), (row,col+1) } - points }
        height += 1
    return height
