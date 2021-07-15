import copy


def add_space(cells):
    row = [[0] * (len(cells[0]) + 2)]
    return row + [[0] + x + [0] for x in cells] + copy.deepcopy(row)


def cut_space(cells):
    for i in range(-1, 1):
        while cells[i].count(1) == 0:
            cells.pop(i)
        while [cells[n][i] for n in range(len(cells))].count(1) == 0:
            for n in range(len(cells)):
                cells[n].pop(i)
    return cells


def morph_cell(neighbours, cell):
    if cell == 1:
        if neighbours.count(1) < 2 or neighbours.count(1) > 3:
            return 0
    if cell == 0 and neighbours.count(1) == 3:
        return 1
    else:
        return cell


def get_neighbours(cells, coords):
    neighbours = []
    for n in range(max(0, coords[0] - 1), min(len(cells), coords[0] + 2)):
        for m in range(max(0, coords[1] - 1), min(len(cells[n]), coords[1] + 2)):
            neighbours.append(cells[n][m])
    if cells[coords[0]][coords[1]] == 1:
        neighbours = sorted(neighbours)[:-1]
    else:
        neighbours = sorted(neighbours)[1:]
    return morph_cell(neighbours, cells[coords[0]][coords[1]])


def new_step(cells, new_cells):
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            new_cells[i][j] = get_neighbours(cells, (i, j))
    return new_cells


def get_generation(cells, generations):
    while generations != 0:
        cells = add_space(cells)
        new_cells = copy.deepcopy(cells)
        new_cells = cut_space(new_step(cells, new_cells))
        cells = new_cells
        print(cells)
        generations -= 1
    return cells
