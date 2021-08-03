def get_diagonale_code(grid: str) -> str:
    matrix = [i.split() for i in grid.split('\n')]
    x, y, flag = 0, 0, 1
    result = ''
    while x < len(matrix) and y < len(matrix[x]):
        result += matrix[x][y]
        x, y = x + flag, y + 1
        flag = flag if 1 < x + 1 < len(matrix) else -flag
    return result
