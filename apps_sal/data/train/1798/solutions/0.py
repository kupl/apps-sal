def get(cells, i, j):
    return cells[i][j] if i > -1 and j > -1 and i < len(cells) and j < len(cells[0]) else 0


def num_neighbors(cells, i, j):
    return (get(cells, i, j + 1) + get(cells, i, j - 1) + get(cells, i + 1, j) +
            get(cells, i - 1, j) + get(cells, i - 1, j - 1) + get(cells, i - 1, j + 1) +
            get(cells, i + 1, j - 1) + get(cells, i + 1, j + 1))


def next_cell(cell, i, j):
    n = num_neighbors(cell, i, j)
    return int(0 if n < 2 or n > 3 else 1 if cell[i][j] else n == 3)


def expand(cells):
    row = [0] * (len(cells[0]) + 2)
    return [row] + [[0] + r + [0] for r in cells] + [row]


def trim(cells):
    while not any(cells[0]):
        del cells[0]
    while not any(cells[-1]):
        del cells[-1]
    while not any([row[0] for row in cells]):
        list(map(lambda x: x.pop(0), cells))
    while not any([row[-1] for row in cells]):
        list(map(lambda x: x.pop(), cells))


def next_gen(cells):
    cells = expand(cells)
    cells = [[next_cell(cells, i, j) for j in range(len(cells[i]))] for i in range(len(cells))]
    trim(cells)
    return cells


def get_generation(cells, generations):
    for i in range(generations):
        cells = next_gen(cells)
    if not cells:
        return [[]]
    return cells
