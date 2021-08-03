def get_diagonale_code(grid: str) -> str:
    if not grid:
        return ""
    lines = [l.split() for l in grid.split('\n')]
    row, col, word = (0, 0, "")
    while col < len(lines[row]):
        word += lines[row][col]
        if row == 0:
            down = True
        if row + 1 == len(lines):
            down = False
        row = row + 1 if down else row - 1
        col += 1
    return word
