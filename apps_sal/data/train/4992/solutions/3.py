def bingo(card, numbers):
    grid = card[1:]
    draw = set(int(n[1:]) for n in numbers if n[0] != "F") | {"FREE SPACE"}
    lines = [set(l) for l in grid]
    columns = [set(c) for c in zip(*grid)]
    diagonals = [set(d[(-1)**p * i] for i, d in enumerate(grid, p)) for p in (0, 1)]
    rows = lines + columns + diagonals
    return any(row.issubset(draw) for row in rows)
