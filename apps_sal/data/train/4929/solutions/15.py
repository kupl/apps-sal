def get_diagonale_code(grid: str) -> str:
    g = (grid.replace(" ","").split("\n"))
    i, j, d, word = 0, 0, 1, ""
    while 0 <= i < len(g) and j < len(g[i]):
        if 0 <= j < len(g[i]):
            word += g[i][j]
            i, j = i + d, j + 1
        else: 
            i += d
        if i == 0 or i == len(g) - 1: 
            d = -d
    return word
