# Today I shall be mostly using geometry, group theory, and massive overkill to solve a problem...

# These are the archetypes of the nets from a cube
nets = [
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 0],
    ],
    [
        [1, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
    ],
    [
        [1, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 0],
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 1],
    ],
    [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
    ],
    [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
    ],
]

# Various transformations we can apply to the nets...


def h_mirror(m):
    # Mirror a matrix horizontally
    return m[::-1]


def v_mirror(m):
    # Mirror a matrix vertically
    return [r[::-1] for r in m]


def transpose(m):
    # Transpose a matrix
    return list(map(list, zip(*m)))


def rotate_cw(m):
    # Rotate a matrix clock-wise
    coords = [(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 1]
    new_coords = normalise([(y, -x) for x, y in coords])
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for x, y in new_coords:
        result[y][x] = 1
    return result


def rotate_ccw(m):
    # Rotate a matrix counter lock-wise
    coords = [(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 1]
    new_coords = normalise([(-y, x) for x, y in coords])
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for x, y in new_coords:
        result[y][x] = 1
    return result


def identity(coords):
    # No transformation
    return coords


def normalise(coords):
    # Translate all coordinates to that all x>=0 and y>=0
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    return tuple([(x - min_x, y - min_y) for x, y in coords])


def compose(*fns):
    # Compose transformations
    def apply(*args, **kwargs):
        result = fns[0](*args, **kwargs)
        for fn in fns[1:]:
            result = fn(result)
        return result
    return apply


# Transformations needed to generate all the symmetries of the nets
compositions = [
    identity,
    h_mirror,
    v_mirror,
    transpose,
    rotate_cw,
    rotate_ccw,
    compose(rotate_cw, rotate_cw),
    compose(rotate_cw, rotate_cw, transpose),
]

# Build all possible transformations of each net
solutions = []
for net in nets:
    for composition in compositions:
        net_prime = composition(net)
        if net_prime not in solutions:
            solutions.append(net_prime)


def to_relative(m):
    # Find the coordinates of the 1s in the supplied matrix
    return tuple(sorted([(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 1]))


# All possible solutions using a relative coordinate system
relative_coordinate_solutions = set(to_relative(s) for s in solutions)


def fold_cube(number_list):
    # Convert from numbered cells to relative coordinates
    relative_coordinates = normalise(sorted([((n - 1) // 5, (n - 1) % 5) for n in number_list]))
    # See if we have a known solution
    return relative_coordinates in relative_coordinate_solutions
