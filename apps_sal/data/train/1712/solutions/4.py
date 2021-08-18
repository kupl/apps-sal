from collections import defaultdict, namedtuple


def puzzle_solver(pieces, width, height):

    catalogue = defaultdict(lambda: defaultdict(dict))

    rows, columns = 0, 0
    for piece in pieces:
        (top_left, top_right), (bottom_left, bottom_right), id = piece
        catalogue[top_left][top_right][bottom_left] = bottom_right, id
        if None is top_left is bottom_left:
            rows += 1
        if None is top_left is top_right:
            columns += 1

    puzzle = tuple([None] * columns for _ in range(rows))

    puzzle[0][0] = catalogue[None][None][None]

    for col in range(1, columns):
        puzzle[0][col] = catalogue[None][None][puzzle[0][col - 1][0]]

    for row in range(1, rows):
        puzzle[row][0] = catalogue[None][puzzle[row - 1][0][0]][None]

    for row in range(1, rows):
        for col in range(1, columns):
            top_left = puzzle[row - 1][col - 1][0]
            top_right = puzzle[row - 1][col][0]
            bottom_left = puzzle[row][col - 1][0]
            puzzle[row][col] = catalogue[top_left][top_right][bottom_left]

    return [tuple(piece[1] for piece in row) for row in puzzle]
