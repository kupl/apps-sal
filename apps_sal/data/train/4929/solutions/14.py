def get_diagonale_code(grid: str) -> str:
    matrix = [i.split() for i in grid.split('\n')]
    x, y = 0, 0
    flag = True
    result = ''
    while x < len(matrix) and y < len(matrix[x]) :
        result += matrix[x][y]
        y += 1
        x = x + 1 if flag else x - 1
        flag = flag if 1 < x + 1 < len(matrix) else not flag
    return result
        
        


