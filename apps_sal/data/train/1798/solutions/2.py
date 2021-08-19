import copy


def pad(cells):
    for x in cells:
        x.append(0)
        x.insert(0, 0)
    cells.append([0] * len(cells[0]))
    cells.insert(0, [0] * len(cells[0]))
    return cells


def trim_world(cells):
    while all((i == 0 for i in cells[0])):
        cells.pop(0)
    while all((i == 0 for i in cells[-1])):
        cells.pop()
    while all((i[0] == 0 for i in cells)):
        cells = [x[1:] for x in cells]
    while all((i[-1] == 0 for i in cells)):
        cells = [x[:-1] for x in cells]
    return cells


def get_generation(cells, generations):
    cells = copy.deepcopy(cells)
    for g in range(generations):
        cells = pad(cells)
        new_world = copy.deepcopy(cells)
        for i in range(len(new_world)):
            for j in range(len(new_world[i])):
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        try:
                            if (k != 0 or l != 0) and i + k > -1 and (j + l > -1) and cells[i + k][j + l]:
                                count += 1
                        except IndexError:
                            'meh'
                new_world[i][j] = cells[i][j] if count == 2 else 1 if count == 3 else 0
        cells = trim_world(new_world)
    return cells
