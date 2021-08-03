def puzzle_solver(pieces, width, height):
    xs, ys, edge = list(range(width)), list(range(height)), ((None, None), (None, None))
    solution_grid = [[None for _ in xs] for _ in ys]
    id_to_piece = {p[2]: (p[0], p[1]) for p in pieces}
    code_to_id = {encode(p[0], p[1][0]): id for id, p in list(id_to_piece.items())}
    for y in ys:
        for x in xs:
            top_piece = id_to_piece[solution_grid[y - 1][x]] if y > 0 else edge
            left_piece = id_to_piece[solution_grid[y][x - 1]] if x > 0 else edge
            solution_grid[y][x] = code_to_id[encode(top_piece[1], left_piece[1][1])]
    return [tuple([solution_grid[y][x] for x in xs]) for y in ys]


def encode(top, left_bottom):
    return f"{top},{left_bottom}"
