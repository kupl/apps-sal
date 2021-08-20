nets = [[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0]], [[1, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]], [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0]], [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1]], [[0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0]], [[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]], [[1, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0]], [[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]], [[1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1]], [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]], [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1]]]


def h_mirror(m):
    return m[::-1]


def v_mirror(m):
    return [r[::-1] for r in m]


def transpose(m):
    return list(map(list, zip(*m)))


def rotate_cw(m):
    coords = [(x, y) for (y, row) in enumerate(m) for (x, v) in enumerate(row) if v == 1]
    new_coords = normalise([(y, -x) for (x, y) in coords])
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for (x, y) in new_coords:
        result[y][x] = 1
    return result


def rotate_ccw(m):
    coords = [(x, y) for (y, row) in enumerate(m) for (x, v) in enumerate(row) if v == 1]
    new_coords = normalise([(-y, x) for (x, y) in coords])
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for (x, y) in new_coords:
        result[y][x] = 1
    return result


def identity(coords):
    return coords


def normalise(coords):
    min_x = min((x for (x, y) in coords))
    min_y = min((y for (x, y) in coords))
    return tuple([(x - min_x, y - min_y) for (x, y) in coords])


def compose(*fns):

    def apply(*args, **kwargs):
        result = fns[0](*args, **kwargs)
        for fn in fns[1:]:
            result = fn(result)
        return result
    return apply


compositions = [identity, h_mirror, v_mirror, transpose, rotate_cw, rotate_ccw, compose(rotate_cw, rotate_cw), compose(rotate_cw, rotate_cw, transpose)]
solutions = []
for net in nets:
    for composition in compositions:
        net_prime = composition(net)
        if net_prime not in solutions:
            solutions.append(net_prime)


def to_relative(m):
    return tuple(sorted([(x, y) for (y, row) in enumerate(m) for (x, v) in enumerate(row) if v == 1]))


relative_coordinate_solutions = set((to_relative(s) for s in solutions))


def fold_cube(number_list):
    relative_coordinates = normalise(sorted([((n - 1) // 5, (n - 1) % 5) for n in number_list]))
    return relative_coordinates in relative_coordinate_solutions
