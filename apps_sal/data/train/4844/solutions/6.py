moves = {"l": (-1, 0), "u": (0, -1), "d": (0, 1), "r": (1, 0)}


def get_password(grid, directions):
    pwd, (x, y) = "", next((row.index("x"), j) for j, row in enumerate(grid) if "x" in row)
    for d in directions:
        x, y = x + moves[d[0]][0], y + moves[d[0]][1]
        if d[-1] == "T":
            pwd = f"{pwd}{grid[y][x]}"
    return pwd
